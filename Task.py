from dataclasses import dataclass
from typing import Union

from Status import Status

DEFAULT_STATUS = Status.NOT_COMPLETED


@dataclass
class Task:
    description: str
    status: Status

    def __init__(self, description: str, status: Union[str, Status] = DEFAULT_STATUS):
        self.description = description
        self.status = self._convert_status(status)

    def _convert_status(self, status: Union[str, Status]) -> Status:
        if isinstance(status, str):
            return Status.from_string(status)
        elif isinstance(status, Status):
            return status
        else:
            raise TypeError("status must be either a str or a Status instance")

    @classmethod
    def from_string(cls, description: str, status: str = DEFAULT_STATUS.value) -> 'Task':
        return cls(description, status)

    @classmethod
    def from_status(cls, description: str, status: Status = DEFAULT_STATUS) -> 'Task':
        return cls(description, status)
