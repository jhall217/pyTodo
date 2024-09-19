from enum import Enum


class Status(Enum):
    COMPLETED = "Complete"
    NOT_COMPLETED = "Not Complete"
    IN_PROGRESS = "In Progress"

    @classmethod
    def _init_status_map(cls):
        cls.STATUS_MAP = {status.value: status for status in Status}

    @classmethod
    def from_string(cls, status_string: str) -> 'Status':
        try:
            return cls.STATUS_MAP[status_string]
        except KeyError:
            raise ValueError(f"'{status_string}' not a valid Status")


Status._init_status_map()
