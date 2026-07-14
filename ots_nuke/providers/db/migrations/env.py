import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import Connection
from sqlalchemy.ext.asyncio import create_async_engine

from ots_nuke.providers.db.meta import meta
from ots_nuke.providers.db.models import load_all_models
from ots_nuke.settings.settings import settings

config = context.config

load_all_models()

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = meta


def run_migrations_offline() -> None:
    """Run migrations in offline mode."""
    context.configure(
        url=settings.db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={'paramstyle': 'named'},
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in online mode."""
    connectable = create_async_engine(settings.db_url)
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def do_run_migrations(connection: Connection) -> None:
    """Run actual migrations."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations() -> None:
    """Run migrations in offline or online mode."""
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        asyncio.run(run_migrations_online())


run_migrations()
