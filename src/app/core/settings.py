from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_ignore_empty=True,
        extra='ignore',
    )

    DATABASE_NAME: str

    @property
    def DATABASE_URL(self) -> str:
        return f'sqlite:///{self.DATABASE_NAME}'


settings = Settings()  # type: ignore
