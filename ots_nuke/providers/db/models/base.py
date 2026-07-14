from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from ots_nuke.providers.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta


class TimeStampMixin:
    """Common timestamp fields for ORM models."""

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        comment='Timestamp when the record was created',
    )
    update_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
        comment='Timestamp when the record was last updated',
    )
