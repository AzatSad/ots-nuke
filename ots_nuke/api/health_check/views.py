from fastapi import APIRouter, status

from ots_nuke.api.health_check.schemas import HealhCheckPingResponse
from ots_nuke.core.enums import ResponseStatusEnum

router = APIRouter()


@router.get(
    '/ping',
    responses={
        status.HTTP_200_OK: {
            'description': 'Сервис доступен.',
        }
    },
)
async def ping() -> HealhCheckPingResponse:
    """Check service available OTS-Nuke."""
    return HealhCheckPingResponse(
        status=ResponseStatusEnum.SUCCESS,
        data='pong',
        message='OTS-Nuke is available',
    )
