from typing import Any

from pydantic import BaseModel, Field

from ots_nuke.core.enums import ResponseStatusEnum


class BaseResponseSchema(BaseModel):
    """Base schema response API."""

    status: ResponseStatusEnum = Field(...)
    data: Any | None = Field(default=None)
    message: str | None = Field(default=None)
    system_message: str | None = Field(alias='systemMessage', default=None)
