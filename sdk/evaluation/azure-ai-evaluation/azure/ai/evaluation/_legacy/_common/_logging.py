# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# Original source:
# - promptflow-core/promptflow/_core/log_manager.py
# - promptflow-core/promptflow/_utils/logger_utils.py

import os
import logging
import sys
from datetime import datetime, timezone
from typing import Any, Final, Optional, Set, TextIO, Tuple, Union


valid_logging_level: Final[Set[str]] = {"CRITICAL", "FATAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG", "NOTSET"}


def get_pf_logging_level(default=logging.INFO):
    logging_level = os.environ.get("PF_LOGGING_LEVEL", None)
    if logging_level not in valid_logging_level:
        # Fall back to info if user input is invalid.
        logging_level = default
    return logging_level


def get_format_for_logger(
    default_log_format: Optional[str] = None, default_date_format: Optional[str] = None
) -> Tuple[str, str]:
    """
    Get the logging format and date format for logger.

    This function attempts to find the handler of the root logger with a configured formatter.
    If such a handler is found, it returns the format and date format used by this handler.
    This can be configured through logging.basicConfig. If no configured formatter is found,
    it defaults to LOG_FORMAT and DATETIME_FORMAT.
    """
    log_format = (
        os.environ.get("PF_LOG_FORMAT")
        or default_log_format
        or "%(asctime)s %(thread)7d %(name)-18s %(levelname)-8s %(message)s"
    )
    datetime_format = os.environ.get("PF_LOG_DATETIME_FORMAT") or default_date_format or "%Y-%m-%d %H:%M:%S %z"
    return log_format, datetime_format


def get_logger(name: str) -> logging.Logger:
    """Get logger used during execution."""
    logger = logging.Logger(name)
    logger.setLevel(get_pf_logging_level())
    stdout_handler = logging.StreamHandler(sys.stdout)
    fmt, datefmt = get_format_for_logger()
    stdout_handler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))
    logger.addHandler(stdout_handler)
    return logger


# Logs by bulk_logger will only be shown in bulktest and eval modes.
# These logs should contain overall progress logs and error logs.
bulk_logger = get_logger("execution.bulk")


def log_progress(
    run_start_time: datetime,
    total_count: int,
    current_count: int,
    logger: logging.Logger = bulk_logger,
    formatter="Finished {count} / {total_count} lines.",
) -> None:
    if current_count > 0:
        delta = datetime.now(timezone.utc).timestamp() - run_start_time.timestamp()
        average_execution_time = round(delta / current_count, 2)
        estimated_execution_time = round(average_execution_time * (total_count - current_count), 2)
        logger.info(formatter.format(count=current_count, total_count=total_count))
        logger.info(
            f"Average execution time for completed lines: {average_execution_time} seconds. "
            f"Estimated time for incomplete lines: {estimated_execution_time} seconds."
        )


def incremental_print(log: str, printed: int, fileout: Union[TextIO, Any]) -> int:
    count = 0
    for line in log.splitlines():
        if count >= printed:
            fileout.write(line + "\n")
            printed += 1
        count += 1
    return printed


def print_red_error(message):
    try:
        from colorama import Fore, init

        init(autoreset=True)
        print(Fore.RED + message)
    except ImportError:
        print(message)
