# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import logging
import sys

from contextlib import AbstractContextManager
from contextvars import ContextVar, Token
from dataclasses import dataclass
from io import StringIO, TextIOBase, TextIOWrapper
from threading import Lock
from typing import Any, Final, List, Optional, Set, Union, overload
from typing_extensions import override
from uuid import uuid4

from ._logging import get_format_for_logger, get_pf_logging_level


_original_stdouts: Final[List[Union[TextIOWrapper, Any]]] = []
_original_stderrs: Final[List[Union[TextIOWrapper, Any]]] = []

_registered_handlers: Final[Set[str]] = set()
_registered_handlers_lock: Final[Lock] = Lock()

_current_stdout: ContextVar[Union[TextIOBase, Any]] = ContextVar("_current_stdout", default=sys.stdout)
_current_stderr: ContextVar[Union[TextIOBase, Any]] = ContextVar("_current_stderr", default=sys.stderr)


class CaptureLogsContext(AbstractContextManager):
    @overload
    def __init__(self, *, parent_logger: logging.Logger, log_entry: int) -> None:
        ...

    @overload
    def __init__(self, *, run_id: str, log_entry: int) -> None:
        ...

    def __init__(
        self,
        *,
        log_entry: int,
        parent_logger: Optional[logging.Logger] = None,
        run_id: Optional[str] = None,
    ) -> None:
        self._captured_logs: StringIO = StringIO()
        self._log_id: str = uuid4().hex
        if parent_logger:
            self._logger = parent_logger.getChild(str(log_entry))
            self._logger.addHandler(logging.StreamHandler(self._captured_logs))
            self._logger.propagate = False
        elif run_id:
            self._logger = logging.Logger(f"{run_id}.{log_entry}")
            self._logger.setLevel(get_pf_logging_level())
            handler = logging.StreamHandler(self._captured_logs)
            handler.setFormatter(logging.Formatter(*get_format_for_logger()))
            self._logger.addHandler(handler)
            self._logger.propagate = False
        else:
            raise ValueError("Either parent_logger or run_id must be provided.")

        self._stdout_tkn: Optional[Token[TextIOBase]] = None
        self._stderr_tkn: Optional[Token[TextIOBase]] = None

    @property
    def logger(self) -> logging.Logger:
        return self._logger

    def get_captured_logs(self) -> str:
        return self._captured_logs.getvalue()

    @override
    def __enter__(self) -> "CaptureLogsContext":
        # First register the current instances TextIOBase as the current context for stdout and stderr
        self._stdout_tkn = _current_stdout.set(self._captured_logs)
        self._stderr_tkn = _current_stderr.set(self._captured_logs)

        with _registered_handlers_lock:
            _registered_handlers.add(self._log_id)
            if len(_registered_handlers) == 1:
                # We are the first handler, so we need to replace the original stdout and stderr with
                # our captured logs interceptor
                _original_stdouts.append(sys.stdout)
                sys.stdout = _BatchEngineStreamInterceptor(False)
                _original_stderrs.append(sys.stderr)
                sys.stderr = _BatchEngineStreamInterceptor(True)

        return self

    @override
    def __exit__(self, exc_type, exc_value, traceback):
        with _registered_handlers_lock:
            _registered_handlers.remove(self._log_id)
            if len(_registered_handlers) == 0:
                # We are the last handler, so we need to replace the original stdout and stderr with
                # the original captured sys.stdout and sys.stderr
                sys.stdout = _original_stdouts.pop()
                sys.stderr = _original_stderrs.pop()

        # Unregister the current instances TextIOBase as the current context for stdout and stderr
        if self._stdout_tkn:
            _current_stdout.reset(self._stdout_tkn)
        if self._stderr_tkn:
            _current_stderr.reset(self._stderr_tkn)


@dataclass
class _BatchEngineStreamInterceptor(TextIOBase):
    """
    This class acts as a replacement for sys.stdout and sys.stderr. It is globally registered as a
    replacement when the batch engine is running. It will check the current log context to determine
    where to write the log message.
    """
    is_std_err: Final[bool]

    @override
    def write(self, message: str) -> int:
        return self._get_writer().write(message)

    @override
    def flush(self) -> None:
        self._get_writer().flush()

    def _get_writer(self) -> Union[TextIOBase, Any]:
        return _current_stderr.get() if self.is_std_err else _current_stdout.get()
