import uuid

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from ots_nuke.providers.db.models.base import Base, TimeStampMixin


class SecretModel(Base, TimeStampMixin):
    """Model for one-time secrets."""

    __tablename__ = 'secrets'

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        comment='Unique secret identifier',
    )
    secret_text: Mapped[str] = mapped_column(
        Text,
        comment='Secret text content',
    )
