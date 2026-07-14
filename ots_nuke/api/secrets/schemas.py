from pydantic import BaseModel, Field

from ots_nuke.core.schemas import BaseResponseSchema


class SecretCreateRequest(BaseModel):
    """Request schema for creating a new secret."""

    secret_text: str = Field(..., min_length=1, max_length=3000)


class SecretCreateData(BaseModel):
    """Data payload for secret creation response."""

    secret_key: str


class SecretCreateResponse(BaseResponseSchema):
    """Responce schema for secret creation schema."""

    data: SecretCreateData


class SecretGetData(BaseModel):
    """Data payload for secret retrieval response."""

    secret_text: str


class SecretGetResponse(BaseResponseSchema):
    """Response schema for secret retrieval endpoint."""

    data: SecretGetData | None = None
