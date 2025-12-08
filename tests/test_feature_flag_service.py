import uuid
from http import HTTPStatus

import pytest
from sqlmodel import Session

from src.app.api.feature_flags.domain.feature_flag_models import FeatureFlag
from src.app.api.feature_flags.exceptions.feature_flag_exceptions import (
    FeatureFlagNotFoundException,
)
from src.app.api.feature_flags.services.feature_flag_services import (
    FeatureFlagService,
)


def test_read_one_should_return_feature_flag(
    session: Session, feature_flag: FeatureFlag
):
    db_feature_flag = FeatureFlagService(session).read_one(feature_flag.id)

    assert db_feature_flag
    assert db_feature_flag.name == feature_flag.name
    assert db_feature_flag.technical_key == feature_flag.technical_key
    assert db_feature_flag.operational_status == (
        feature_flag.operational_status
    )


def test_read_should_return_not_found_exception(session: Session):
    random_uuid = uuid.uuid4()

    with pytest.raises(FeatureFlagNotFoundException) as error:
        FeatureFlagService(session).read_one(random_uuid)

    assert error.value.message == 'feature flag not found'
    assert error.value.code == HTTPStatus.NOT_FOUND
