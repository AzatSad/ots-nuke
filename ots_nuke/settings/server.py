import enum
from pydantic_settings import BaseSettings


@enum.unique
class LogLevel(enum.StrEnum):
    """Logs level"""

    NOTSET = 'NOTSET'
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    FATAL = 'FATAL'

class ServerSettings(BaseSettings):
    host: str = '0.0.0.0'
    port: int = 8000
    workers_count: int = 1
    reload: bool = False
    log_level: LogLevel = LogLevel.INFO
