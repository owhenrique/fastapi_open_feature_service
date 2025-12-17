from http import HTTPStatus

import pytest
from sqlmodel import Session

from app.api.v1.feature_flags.domain.flag_model import (
    Flag,
    OperationalStatusEnum,
)
from app.api.v1.feature_flags.exceptions.flag_exceptions import (
    FlagNotFoundException,
)
from app.api.v1.feature_flags.repositories.flag_repository import (
    FlagRepository,
)
from app.api.v1.feature_flags.services.flag_service import (
    FlagService,
)


def test_read_one_should_return_flag(session: Session, flag: Flag):
    repository = FlagRepository(session)
    service = FlagService(repository)
    db_flag = service.read_one(flag.technical_key)

    assert db_flag
    assert db_flag.name == flag.name
    assert db_flag.technical_key == flag.technical_key
    assert db_flag.operational_status == flag.operational_status


def test_read_should_return_not_found_exception(session: Session):
    repository = FlagRepository(session)
    service = FlagService(repository)

    with pytest.raises(FlagNotFoundException) as error:
        service.read_one('another-flag')

    assert error.value.message == 'flag not found'
    assert error.value.code == HTTPStatus.NOT_FOUND


def test_is_enabled_should_return_true(session: Session, flag: Flag):
    repository = FlagRepository(session)
    service = FlagService(repository)

    flag_is_enabled = service.is_enabled(flag.technical_key)

    assert flag_is_enabled is True
    assert flag.operational_status == OperationalStatusEnum.ON


def test_is_enabled_should_return_false(session: Session, another_flag: Flag):
    repository = FlagRepository(session)
    service = FlagService(repository)

    flag_isnt_enabled = service.is_enabled(another_flag.technical_key)

    assert flag_isnt_enabled is False
    assert another_flag.operational_status == OperationalStatusEnum.OFF


def test_is_enabled_should_return_not_found_exception(session: Session):
    repository = FlagRepository(session)
    service = FlagService(repository)

    with pytest.raises(FlagNotFoundException) as error:
        service.is_enabled('another-flag')

    assert error.value.message == 'flag not found'
    assert error.value.code == HTTPStatus.NOT_FOUND
