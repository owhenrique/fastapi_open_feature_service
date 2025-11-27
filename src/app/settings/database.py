from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='database.env', env_file_encoding='utf-8', extra='ignore'
    )

    DATABASE_FILE_URL: str
