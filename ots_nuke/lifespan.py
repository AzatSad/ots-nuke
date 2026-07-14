from __future__ import annotations

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from ots_nuke.__version__ import show_project_logo
from ots_nuke.log import logger
from ots_nuke.providers.db.lifespan import setup_db

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from fastapi import FastAPI


@asynccontextmanager
async def lifespan_setup(
    app: FastAPI,
) -> AsyncGenerator[None]:
    """Move start and stop aplication."""
    show_project_logo()
    logger.info('Application started')
    setup_db(app)

    yield

    logger.info('Application stopped')
