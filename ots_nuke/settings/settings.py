from typing import final

from pydantic_settings import BaseSettings, SettingsConfigDict

from ots_nuke.settings.server import ServerSettings


@final
class Settings(ServerSettings, BaseSettings):
    """The main settings class.

    Loads configuration from environment variavels
    and the .env file with the OTS_NUKE_ prefix.
    """

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='OTS_NUKE_',
        env_file_encoding='utf-8',
        extra='ignore',
    )


settings = Settings()
