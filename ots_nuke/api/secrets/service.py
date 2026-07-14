import uuid

from ots_nuke.providers.db.dao.secret_dao import SecretDAO


class SecretService:
    """Service layer for secret operations."""

    def __init__(self, dao: SecretDAO) -> None:
        self._dao = dao

    async def create(self, secret_text: str) -> str:
        """Create a new secret and return its key."""
        secret = await self._dao.create(secret_text=secret_text)
        return secret.id.hex

    async def get(self, secret_key: str) -> str | None:
        """Get and delete a one-time secret."""
        try:
            secret_id = uuid.UUID(secret_key)
        except ValueError:
            return None
        secret = await self._dao.get_by_id(secret_id=secret_id)
        if secret is None:
            return None
        await self._dao.delete(secret=secret)
        return secret.secret_text

    async def get_without_delete(self, secret_key: str) -> str | None:
        """Check if secret exists without deleting it."""
        try:
            secret_id = uuid.UUID(secret_key)
        except ValueError:
            return None
        secret = await self._dao.get_by_id(secret_id=secret_id)
        if secret is None:
            return None
        return secret.secret_text
