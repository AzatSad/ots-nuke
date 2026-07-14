import uuid
from typing import Annotated

from fastapi import Depends
from sqlalchemy import select

from ots_nuke.providers.db.dao.base import BaseDAO
from ots_nuke.providers.db.deps import DBSessionDepends
from ots_nuke.providers.db.models.secret_model import SecretModel


class SecretDAO(BaseDAO):
    """Data access object for secrets."""

    async def create(self, secret_text: str) -> SecretModel:
        """Create a new secret."""
        secret = SecretModel(secret_text=secret_text)
        self.session.add(secret)
        await self.session.flush()
        return secret

    async def get_by_id(self, secret_id: uuid.UUID) -> SecretModel | None:
        """Get secret by ID."""
        result = await self.session.execute(
            select(SecretModel).where(SecretModel.id == secret_id),
        )
        return result.scalar_one_or_none()

    async def delete(self, secret: SecretModel) -> None:
        """Delete a secret."""
        await self.session.delete(secret)
        await self.session.flush()


def get_secret_dao(session: DBSessionDepends) -> SecretDAO:
    """FastAPI dependency for SecretDAO."""
    return SecretDAO(session=session)


SecretDAODepends = Annotated[SecretDAO, Depends(get_secret_dao)]
