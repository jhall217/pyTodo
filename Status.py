from enum import Enum


class Status(Enum):
    COMPLETED = "Complete"
    NOT_COMPLETED = "Not Complete"
    IN_PROGRESS = "In Progress"

    @classmethod
    def initialize_status_map(cls):
        if not hasattr(cls, 'STATUS_MAP'):
            cls.STATUS_MAP = {status.value: status for status in Status}

    @classmethod
    def from_string(cls, status_string: str) -> 'Status':
        cls.initialize_status_map()
        try:
            return cls.STATUS_MAP[status_string]
        except KeyError:
            raise ValueError(f"'{status_string}' not a valid Status")
