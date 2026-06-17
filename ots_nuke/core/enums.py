import enum


@enum.unique
class ResponseStatusEnum(enum.Enum):
    """Status API response"""

    SUCCESS = 'success'
    FAIL = 'fail'
