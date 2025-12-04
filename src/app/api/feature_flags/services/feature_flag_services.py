from sqlmodel import Session

from app.api.feature_flags.domain.feature_flag_models import FeatureFlag
from app.api.feature_flags.exceptions.feature_flag_exceptions import (
    FeatureFlagAlreadyExistsException,
)
from app.api.feature_flags.repositories.feature_flag_repositories import (
    FeatureFlagRepositorie,
)
from app.api.feature_flags.schemas.feature_flag_schemas import (
    FeatureFlagCreateSchema,
)


class FeatureFlagService:
    def __init__(self, session: Session):
        self._session = session
        self._repositorie = FeatureFlagRepositorie(self._session)

    def create(self, feature_flag: FeatureFlagCreateSchema) -> FeatureFlag:
        # Todo: change featureflagcreateschema to feature flag entity/model
        # decloupling
        if (self._repositorie.get_by_name(feature_flag.name) is not None) or (
            self._repositorie.get_by_technical_key(feature_flag.technical_key)
        ) is not None:
            raise FeatureFlagAlreadyExistsException

        instance = FeatureFlag(
            name=feature_flag.name,
            technical_key=feature_flag.technical_key,
            operational_status=feature_flag.operational_status,
        )

        self._repositorie.add(instance)
        self._session.commit()
        self._session.refresh(instance)

        return instance

    def read_all(self):
        return {'feature_flags': self._repositorie.get_all(self._session)}
