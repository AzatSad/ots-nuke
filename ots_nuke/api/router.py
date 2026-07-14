from fastapi.routing import APIRouter

from ots_nuke.api.health_check.views import router as health_check_router
from ots_nuke.api.secrets.views import router as secrets_router

api_router = APIRouter()
api_router.include_router(health_check_router, prefix='/health-check', tags=['health_check'])
api_router.include_router(secrets_router, prefix='/secrets', tags=['secrets'])
