from datetime import datetime

from pydantic import BaseModel


class FeatureFlagPublicSchema(BaseModel):
    description: str
    operational_status: bool


class FeatureFlagCreateSchema(FeatureFlagPublicSchema):
    pass


class FeatureFlagResponseSchema(FeatureFlagPublicSchema):
    id: int
    created_at: datetime
    updated_at: datetime


class FeatureFlagsResponseSchema(BaseModel):
    flags: list[FeatureFlagResponseSchema]
