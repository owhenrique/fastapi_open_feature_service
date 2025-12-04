from enum import StrEnum
from uuid import UUID, uuid4

from sqlmodel import Field

from src.app.models.timestamp_mixin import TimeStampMixin


class OperationalStatusEnum(StrEnum):
    ON = 'on'
    OFF = 'off'
    SEGMENTED = 'segmented'
    ARCHIVED = 'archived'
    PERCENTUAL_ROLLOUT = 'percentual_rollout'


class FeatureFlag(TimeStampMixin, table=True):
    # Todo: write this model a docstring

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True)
    technical_key: str = Field(index=True, unique=True)
    operational_status: OperationalStatusEnum
