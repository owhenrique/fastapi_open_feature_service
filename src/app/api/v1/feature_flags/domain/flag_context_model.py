from pydantic import BaseModel, Field


class FlagContext(BaseModel):
    environment: str | None = Field(min_length=1)
    actor: str | None = Field(min_length=1)
