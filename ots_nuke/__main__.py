import uvicorn

from ots_nuke.settings.settings import settings


def main() -> None:
    """Application entry point."""
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


if __name__ == '__main__':
    main()
