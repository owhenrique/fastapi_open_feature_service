from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

from app.api.feature_flags.domain.feature_flag_models import (
    FeatureFlag,  # noqa: F401
)
from app.core.settings import settings

engine = create_engine(settings.DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


DBSession = Annotated[Session, Depends(get_session)]
