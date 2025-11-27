from datetime import datetime

from pydantic import BaseModel


class FlagPublic(BaseModel):
    description: str
    operational_status: bool


class FlagCreate(FlagPublic):
    pass


class FlagRead(FlagPublic):
    id: int
    created_at: datetime
    updated_at: datetime


class FlagsRead(BaseModel):
    flags: list[FlagRead]
