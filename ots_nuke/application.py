from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from ots_nuke.__version__ import NAME, VERSION
from ots_nuke.api.pages.views import router as pages_router
from ots_nuke.api.router import api_router
from ots_nuke.lifespan import lifespan_setup


def get_app() -> FastAPI:
    """FastAPI application factory."""

    @asynccontextmanager
    async def lifespan(application: FastAPI) -> AsyncGenerator[None]:
        """Lifespan wrapper for FastAPI."""
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

    app.mount('/static', StaticFiles(directory='ots_nuke/static'), name='static')
    app.include_router(router=api_router, prefix='/api')
    app.include_router(router=pages_router)

    return app
