from contextlib import contextmanager
from datetime import datetime
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import event
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.api.v1.feature_flags.domain.flag_model import (
    Flag,
    OperationalStatusEnum,
)
from src.app.core.database import get_session
from src.app.main import app


@pytest.fixture(name='session')
def session_fixture() -> Generator[Session, None, None]:
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    SQLModel.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture(name='client')
def client_fixture(session: Session) -> Generator[TestClient, None, None]:
    def get_db_override():
        return session

    app.dependency_overrides[get_session] = get_db_override

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


@contextmanager
def _mock_db_time(*, model, time=datetime(2025, 1, 1)):
    target_model = model

    def fake_time_handler(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = time
        if hasattr(target, 'updated_at'):
            target.updated_at = time

    event.listen(target_model, 'before_insert', fake_time_handler)

    yield time

    event.remove(target_model, 'before_insert', fake_time_handler)


@pytest.fixture
def mock_db_time():
    return _mock_db_time


@pytest.fixture
def flag(session) -> Flag:
    flag = Flag(
        name='test-flag-red',
        technical_key='tff00',
        operational_status=OperationalStatusEnum.ON,
    )
    session.add(flag)
    session.commit()
    session.refresh(flag)

    return flag


@pytest.fixture
def another_flag(session) -> Flag:
    flag = Flag(
        name='test-another-flag-red',
        technical_key='another-tff00',
        operational_status=OperationalStatusEnum.ON,
    )
    session.add(flag)
    session.commit()
    session.refresh(flag)

    return flag
