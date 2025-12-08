from sqlmodel import Session

from src.app.api.feature_flags.domain.feature_flag_models import FeatureFlag
from src.app.api.feature_flags.repositories.feature_flag_repositories import (
    FeatureFlagRepositorie,
)


def test_get_by_id_should_return_feature_flag(
    session: Session, feature_flag: FeatureFlag
):
    db_feature_flag = FeatureFlagRepositorie(session).get_by_id(
        feature_flag.id
    )

    assert db_feature_flag
    assert db_feature_flag.name == feature_flag.name
    assert db_feature_flag.technical_key == feature_flag.technical_key
    assert db_feature_flag.operational_status == (
        feature_flag.operational_status
    )
