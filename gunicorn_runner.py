from typing import Any

import httptools  # type: ignore[import-untyped]
import uvloop
from gunicorn.app.base import BaseApplication
from gunicorn.util import import_app
from uvicorn.workers import UvicornWorker as BaseUvicornWorker


class UvicornWorker(BaseUvicornWorker):
    """Uvicorn worker with uvloop and httptools."""

    CONFIG_KWARGS: dict[str, Any] = {  # type: ignore[misc] # noqa: RUF012
        'loop': uvloop.__name__,
        'http': httptools.__name__,
        'lifespan': 'on',
        'factory': True,
        'proxy_headers': False,
    }


class GunicornApplication(BaseApplication):
    """Custom Gunicorn application."""

    def __init__(
        self,
        app: str,
        host: str,
        port: int,
        workers: int,
        **kwargs: Any,  # noqa: ANN401
    ) -> None:
        self.options: dict[str, Any] = {
            'bind': f'{host}:{port}',
            'workers': workers,
            'worker_class': 'ots_nuke.gunicorn_runner.UvicornWorker',
            **kwargs,
        }
        self.app = app
        super().__init__()

    def load_config(self) -> None:
        """Load Gunicorn configuration from options."""
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self) -> str:  # type: ignore[override]
        """Load the ASGI application."""
        return import_app(self.app)  # type: ignore[return-value]
