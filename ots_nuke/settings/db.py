from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    """Database connection settings."""

    db_host: str
    db_port: int
    db_user: str
    db_pass: str
    db_base: str
    db_echo: bool

    @property
    def db_url(self) -> str:
        """Assemble database URL from settings."""
        return f'postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_base}'
