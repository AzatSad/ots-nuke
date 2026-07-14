import uvicorn

from ots_nuke.gunicorn_runner import GunicornApplication
from ots_nuke.settings.settings import settings


def main() -> None:
    """Uvicorn entry point."""
    if settings.reload:
        uvicorn.run(
            'ots_nuke.application:get_app',
            host=settings.host,
            port=settings.port,
            workers=settings.workers_count,
            reload=settings.reload,
            log_level=settings.log_level.value.lower(),
            factory=True,
            log_config=None,
        )
    else:
        GunicornApplication(
            app='ots_nuke.application:get_app',
            host=settings.host,
            port=settings.port,
            workers=settings.workers_count,
        ).run()


if __name__ == '__main__':
    main()
