from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.api.v1.feature_flags.domain.flag_model import (
    OperationalStatusEnum,
)


class FlagPublicSchema(BaseModel):
    name: str
    technical_key: str
    operational_status: OperationalStatusEnum


class FlagCreateSchema(FlagPublicSchema):
    operational_status: OperationalStatusEnum = OperationalStatusEnum.OFF


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


class FlagIsEnabledResponseSchema(BaseModel):
    is_enabled: bool


class FlagValueResponseSchema(BaseModel):
    technical_key: str
    is_enabled: bool
