from datetime import datetime

from sqlmodel import Field, SQLModel


class FeatureFlag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str
    operational_status: bool
    created_at: datetime
    updated_at: datetime
