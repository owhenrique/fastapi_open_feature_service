from uuid import UUID

from sqlmodel import Session

from src.app.api.feature_flags.domain.feature_flag_models import FeatureFlag
from src.app.api.feature_flags.exceptions.feature_flag_exceptions import (
    FeatureFlagAlreadyExistsException,
    FeatureFlagNotFoundException,
)
from src.app.api.feature_flags.repositories.feature_flag_repositories import (
    FeatureFlagRepositorie,
)
from src.app.api.feature_flags.schemas.feature_flag_schemas import (
    FeatureFlagCreateSchema,
    FeatureFlagUpdateSchema,
)


class FeatureFlagService:
    def __init__(self, session: Session):
        self._session = session
        self._repositorie = FeatureFlagRepositorie(self._session)

    def create(self, feature_flag: FeatureFlagCreateSchema) -> FeatureFlag:
        # Todo: change featureflagcreateschema to feature flag entity/model
        # decloupling
        if (
            self._repositorie.get_by_name_or_technical_key(
                feature_flag.name, feature_flag.technical_key
            )
            is not None
        ):
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
        return {'feature_flags': self._repositorie.get_all()}

    def read_one(self, feature_flag_id: UUID) -> FeatureFlag:
        instance = self._repositorie.get_by_id(feature_flag_id)

        if instance is None:
            raise FeatureFlagNotFoundException

        return instance

    def update(
        self, feature_flag_id: UUID, feature_flag: FeatureFlagUpdateSchema
    ) -> FeatureFlag:
        instance = self._repositorie.get_by_id(feature_flag_id)

        if instance is None:
            raise FeatureFlagNotFoundException
        # Todo: check if the user found is different than the actual user
        if (
            self._repositorie.get_by_name_or_technical_key(
                feature_flag.name, feature_flag.technical_key
            )
            is not None
        ):
            raise FeatureFlagAlreadyExistsException

        if feature_flag.name:
            instance.name = feature_flag.name
        if feature_flag.technical_key:
            instance.technical_key = feature_flag.technical_key
        if feature_flag.operational_status:
            instance.operational_status = feature_flag.operational_status

        self._repositorie.update(instance)
        self._session.commit()
        self._session.refresh(instance)

        return instance

    def delete(self, feature_flag_id: UUID) -> None:
        instance = self._repositorie.get_by_id(feature_flag_id)

        if instance is None:
            raise FeatureFlagNotFoundException

        self._repositorie.delete(instance)
        self._session.commit()
