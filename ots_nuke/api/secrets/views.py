from fastapi import APIRouter, Response, status

from ots_nuke.api.secrets.schemas import (
    SecretCreateData,
    SecretCreateRequest,
    SecretCreateResponse,
    SecretGetData,
    SecretGetResponse,
)
from ots_nuke.api.secrets.service import SecretService
from ots_nuke.core.enums import ResponseStatusEnum
from ots_nuke.providers.db.dao.secret_dao import SecretDAODepends

router = APIRouter()


@router.post(
    '/',
    responses={
        status.HTTP_201_CREATED: {
            'description': 'Секрет успешно создан.',
        },
    },
)
async def create_secret(
    secret_request: SecretCreateRequest,
    dao: SecretDAODepends,
    response: Response,
) -> SecretCreateResponse:
    """Create a one-time secret."""
    service = SecretService(dao=dao)
    secret_key = await service.create(secret_text=secret_request.secret_text)
    response.status_code = status.HTTP_201_CREATED
    return SecretCreateResponse(
        status=ResponseStatusEnum.SUCCESS,
        data=SecretCreateData(secret_key=secret_key),
        message='Secret created successfully',
    )


@router.get(
    '/{secret_key}',
    responses={
        status.HTTP_200_OK: {
            'description': 'Секрет найден и возвращён.',
        },
        status.HTTP_404_NOT_FOUND: {
            'description': 'Секрет не найден или уже был прочитан.',
        },
    },
)
async def get_secret(
    secret_key: str,
    dao: SecretDAODepends,
    response: Response,
) -> SecretGetResponse:
    """Get a one-time secret using a key."""
    service = SecretService(dao=dao)
    secret_text = await service.get(secret_key=secret_key)
    if secret_text is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return SecretGetResponse(
            status=ResponseStatusEnum.FAIL,
            message='Secret not found or already read.',
        )
    return SecretGetResponse(
        status=ResponseStatusEnum.SUCCESS,
        data=SecretGetData(secret_text=secret_text),
        message='Secret retrieved successfully.',
    )
