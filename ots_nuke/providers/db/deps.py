from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request


async def get_db_session(
    request: Request,
) -> AsyncGenerator[AsyncSession]:
    """Create and yield database session for request lifecycle."""
    session: AsyncSession = request.app.state.db_session_factory()

    try:
        yield session
    finally:
        await session.commit()
        await session.close()


DBSessionDepends = Annotated[AsyncSession, Depends(get_db_session)]
