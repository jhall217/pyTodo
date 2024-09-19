from dataclasses import dataclass
from typing import Union

from Status import Status


@dataclass
class Task:
    description : str
    status : Status

    def __init__(self, description: str, status: Union[str, Status] = 'Not Complete'):
        self.description = description
        if isinstance(status, str):
            self.status = Status.from_string(status)
        elif isinstance(status, Status):
            self.status = status
        else:
            raise TypeError("status must be either a str or a Status instance")

    @classmethod
    def from_strings(cls, description: str, status: str = 'Not Complete') -> 'Task':
        return cls(description, status)

    @classmethod
    def from_status(cls, description: str, status: Status = Status.NOT_COMPLETED) -> 'Task':
        return cls(description, status)
