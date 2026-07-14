from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from ots_nuke.settings.settings import settings


def setup_db(app: FastAPI) -> None:
    """Create connection to the database."""
    engine = create_async_engine(
        settings.db_url,
        echo=settings.db_echo,
    )
    session_factory = async_sessionmaker(
        engine,
        expire_on_commit=False,
    )
    app.state.db_engine = engine
    app.state.db_session_factory = session_factory
