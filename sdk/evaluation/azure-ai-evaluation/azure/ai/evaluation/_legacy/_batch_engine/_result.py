# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Mapping, Optional, Sequence

from ._status import BatchStatus


@dataclass
class TokenMetrics:
    """The token metrics of a run."""

    prompt_tokens: int
    """The number of tokens used in the prompt for the run."""
    completion_tokens: int
    """The number of tokens used in the completion for the run."""
    total_tokens: int
    """The total number of tokens used in the run."""

    def update(self, other: "TokenMetrics") -> None:
        """Update the token metrics with another set of token metrics."""
        self.prompt_tokens += other.prompt_tokens
        self.completion_tokens += other.completion_tokens
        self.total_tokens += other.total_tokens


@dataclass
class BatchRunError:
    """The error of a batch run."""

    details: str
    """The details of the error."""
    exception: Optional[BaseException]
    """The exception of the error."""


@dataclass
class BatchRunDetails:
    """The error of a line in a batch run."""

    id: str
    """The ID of the line run."""
    status: BatchStatus
    """The status of the line run."""
    result: Optional[Mapping[str, Any]]
    """The result of the line run."""
    start_time: Optional[datetime]
    """The start time of the line run. If this was never started, this should be None."""
    end_time: Optional[datetime]
    """The end time of the line run. If this never completed, this should be None."""
    tokens: TokenMetrics
    """The token metrics of the line run."""
    error: Optional[BatchRunError]
    """The error of the line run. This will only be set if the status is Failed."""
    logs: str = ""
    """The logs of the line run"""

    @property
    def duration(self) -> timedelta:
        """The duration of the line run."""
        if self.start_time is not None and self.end_time is not None:
            return self.end_time - self.start_time
        return timedelta(0)

    @staticmethod
    def create_id(run_id: str, index: int) -> str:
        """Helper method to create the ID for a line run."""
        return f"{run_id}_{index}"

    def as_summary_dict(self) -> Mapping[str, Any]:
        """Get the summary of the line run."""
        ret: Dict[str, Any] = {
            "id": self.id,
            "status": self.status.name,
            "duration": str(self.duration),
            "logs": [log for log in self.logs.split("\n") if log],
        }

        if self.error:
            ret["error"] = {
                "details": self.error.details,
                "exception": str(self.error.exception) if self.error.exception else None,
            }

        return ret


@dataclass
class BatchResult:
    """The result of a batch run."""

    status: BatchStatus
    """The overall status of the batch run."""
    total_lines: int
    """The total number of lines in the batch run."""
    failed_lines: int
    """The number of failed lines in the batch run."""
    start_time: datetime
    """The start time of the batch run."""
    end_time: datetime
    """The end time of the batch run."""
    tokens: TokenMetrics
    """The overall token metrics of the batch run."""
    details: Sequence[BatchRunDetails]
    """The details of each line in the batch run."""
    error: Optional[Exception] = None
    """The error of the batch run. This will only be set if the status does not indicate success."""

    @property
    def duration(self) -> timedelta:
        """The duration of the batch run."""
        if self.start_time is not None and self.end_time is not None:
            return self.end_time - self.start_time
        return timedelta(0)

    @property
    def results(self) -> Sequence[Optional[Mapping[str, Any]]]:
        """The results of the batch run."""
        if not self.details:
            return []
        return [d.result for d in self.details]

    @staticmethod
    def from_exception(exception: Exception, start_time: datetime, total_lines: int) -> "BatchResult":
        """Create a BatchResult from an exception."""
        return BatchResult(
            status=BatchStatus.Failed,
            total_lines=total_lines,
            failed_lines=total_lines,
            start_time=start_time,
            end_time=datetime.now(timezone.utc),
            tokens=TokenMetrics(0, 0, 0),
            details=[],
            error=exception,
        )

    def as_error_dict(self) -> Mapping[str, Any]:
        """Get a summary of the batch result errors."""
        return {
            "status": self.status.name,
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "error": str(self.error) if self.error else None,
            "details": [
                detail.as_summary_dict()
                for detail in self.details
                if detail and BatchStatus.is_failed(detail.status) 
            ]
        }
