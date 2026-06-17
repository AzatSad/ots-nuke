from typing import Final

import structlog
from structlog.typing import Processor

from ots_nuke.settings.settings import settings

type OrderedStructLogProcessors = tuple[Processor, ...]


PROCESSORS: Final[OrderedStructLogProcessors] = (
    structlog.contextvars.merge_contextvars,
    structlog.processors.add_log_level,
    structlog.processors.TimeStamper(fmt='iso', utc=False),
    structlog.processors.StackInfoRenderer(),
)

PROCESSORS_DEV: Final[OrderedStructLogProcessors] = (structlog.dev.ConsoleRenderer(colors=True),)

PROCESSORS_JSON: Final[OrderedStructLogProcessors] = (
    structlog.processors.format_exc_info,
    structlog.processors.JSONRenderer(),
)


def _build_processors() -> OrderedStructLogProcessors:
    """Build processor logs."""
    if settings.log_level.value == 'DEBUG':
        return PROCESSORS + PROCESSORS_DEV
    return PROCESSORS + PROCESSORS_JSON


structlog.configure(
    processors=_build_processors(),
    wrapper_class=structlog.stdlib.BoundLogger,
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
    cache_logger_on_first_use=True,
)

logger: structlog.stdlib.BoundLogger = structlog.get_logger()
