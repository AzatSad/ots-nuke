from typing import Annotated

from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from ots_nuke.api.secrets.service import SecretService
from ots_nuke.providers.db.dao.secret_dao import SecretDAODepends

router = APIRouter()
templates = Jinja2Templates(directory='ots_nuke/templates')


@router.get('/', response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """Render main page with secret creation form."""
    return templates.TemplateResponse(request, 'index.html')


@router.post('/', response_class=HTMLResponse)
async def create_secret(
    _request: Request,
    dao: SecretDAODepends,
    secret_text: Annotated[str, Form()],
) -> RedirectResponse:
    """Create a secret and redirect to created page."""
    service = SecretService(dao=dao)
    secret_key = await service.create(secret_text=secret_text)
    return RedirectResponse(
        url=f'/created/{secret_key}',
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.get('/created/{secret_key}', response_class=HTMLResponse)
async def created(request: Request, secret_key: str) -> HTMLResponse:
    """Render page with secret link."""
    secret_url = f'{request.base_url}s/{secret_key}'
    return templates.TemplateResponse(
        request,
        'created.html',
        {'secret_url': secret_url},
    )


@router.get('/s/{secret_key}', response_class=HTMLResponse)
async def reveal_page(
    request: Request,
    dao: SecretDAODepends,
    secret_key: str,
) -> HTMLResponse:
    """Show reveal page without reading the secret."""
    service = SecretService(dao=dao)
    secret_text = await service.get_without_delete(secret_key=secret_key)
    if secret_text is None:
        return templates.TemplateResponse(
            request,
            'not_found.html',
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return templates.TemplateResponse(
        request,
        'reveal.html',
        {'secret_key': secret_key},
    )


@router.post('/s/{secret_key}', response_class=HTMLResponse)
async def get_secret(
    request: Request,
    dao: SecretDAODepends,
    secret_key: str,
) -> HTMLResponse:
    """Get and display a one-time secret, then delete it."""
    service = SecretService(dao=dao)
    secret_text = await service.get(secret_key=secret_key)
    if secret_text is None:
        return templates.TemplateResponse(
            request,
            'not_found.html',
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return templates.TemplateResponse(
        request,
        'secret.html',
        {'secret_text': secret_text},
    )
