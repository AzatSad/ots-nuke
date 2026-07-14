from sqlalchemy.ext.asyncio import AsyncSession


class BaseDAO:
    """Base class for all DAOs."""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session
