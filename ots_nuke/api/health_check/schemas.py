from ots_nuke.core.schemas import BaseResponseSchema


class HealhCheckPingResponse(BaseResponseSchema):
    """Schemas response ping-request"""

    data: str | None = None
