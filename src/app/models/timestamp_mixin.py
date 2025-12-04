from datetime import datetime

import sqlalchemy as sa
from sqlmodel import Field, SQLModel


class TimeStampMixin(SQLModel):
    created_at: datetime | None = Field(
        default=None,
        sa_type=sa.DATETIME(timezone=True),
        sa_column_kwargs={'server_default': sa.func.now()},
    )
    updated_at: datetime | None = Field(
        default=None,
        sa_type=sa.DATETIME(timezone=True),
        sa_column_kwargs={
            'onupdate': sa.func.now(),
            'server_default': sa.func.now(),
        },
    )
