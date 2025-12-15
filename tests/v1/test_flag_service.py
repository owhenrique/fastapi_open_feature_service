from http import HTTPStatus

import pytest
from sqlmodel import Session

from app.api.v1.feature_flags.domain.flag_model import Flag
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
        service.read_one('other-flag')

    assert error.value.message == 'flag not found'
    assert error.value.code == HTTPStatus.NOT_FOUND
