from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.app.api.feature_flags.domain.feature_flag_models import (
    OperationalStatusEnum,
)


class FeatureFlagPublicSchema(BaseModel):
    name: str
    technical_key: str
    operational_status: OperationalStatusEnum


class FeatureFlagCreateSchema(FeatureFlagPublicSchema):
    pass


class FeatureFlagUpdateSchema(BaseModel):
    name: str | None = None
    technical_key: str | None = None
    operational_status: OperationalStatusEnum | None = None


class FeatureFlagResponseSchema(FeatureFlagPublicSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class FeatureFlagsResponseSchema(BaseModel):
    feature_flags: list[FeatureFlagResponseSchema]

    model_config = ConfigDict(from_attributes=True)
