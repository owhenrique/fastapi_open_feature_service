from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.api.feature_flags.domain.flag_model import (
    OperationalStatusEnum,
)


class FlagPublicSchema(BaseModel):
    name: str
    technical_key: str
    operational_status: OperationalStatusEnum


class FlagCreateSchema(FlagPublicSchema):
    pass


class FlagUpdateSchema(BaseModel):
    name: str | None = None
    technical_key: str | None = None
    operational_status: OperationalStatusEnum | None = None


class FlagResponseSchema(FlagPublicSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class FlagsResponseSchema(BaseModel):
    flags: list[FlagResponseSchema]

    model_config = ConfigDict(from_attributes=True)
