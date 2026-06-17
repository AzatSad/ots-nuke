from collections.abc import AsyncGenerator 
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ots_nuke.__version__ import NAME,VERSION
from ots_nuke.api.router import api_router
from ots_nuke.lifespan import lifespan_setup
from ots_nuke.settings.settings import settings


def get_app() -> FastAPI:
    """FastAPI application factory. 
    The main application constructor
    """

    @asynccontextmanager
    async def lifespan(application: FastAPI) -> AsyncGenerator[None]:
        """Lifespan wrapper for FastAPI"""
        async with lifespan_setup(application):
            yield

    app = FastAPI(
        title=NAME,
        version=VERSION,
        lifespan=lifespan,
        docs_url='/api/docs',
        redoc_url='/api/redoc',
        openapi_url='/api/openapi.json',
    )

    app.include_router(router=api_router, prefix='/api')

    return app
    