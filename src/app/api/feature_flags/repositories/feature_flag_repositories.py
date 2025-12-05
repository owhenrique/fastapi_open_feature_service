from typing import Sequence
from uuid import UUID

from sqlmodel import select

from src.app.api.feature_flags.domain.feature_flag_models import FeatureFlag


class FeatureFlagRepositorie:
    def __init__(self, session):
        self._session = session

    def add(self, entity: FeatureFlag) -> None:
        self._session.add(entity)

    def get_by_id(self, id: UUID) -> FeatureFlag | None:
        return self._session.exec(
            select(FeatureFlag).where(FeatureFlag.id == id)
        ).first()

    def get_by_name(self, name: str) -> FeatureFlag | None:
        return self._session.exec(
            select(FeatureFlag).where(FeatureFlag.name == name)
        ).first()

    def get_by_technical_key(self, technical_key: str) -> FeatureFlag | None:
        return self._session.exec(
            select(FeatureFlag).where(
                FeatureFlag.technical_key == technical_key
            )
        ).first()

    def get_all(self) -> Sequence[FeatureFlag] | Sequence[None]:
        return self._session.exec(select(FeatureFlag)).all()

    def update(self, entity: FeatureFlag) -> None:
        self._session.add(entity)
