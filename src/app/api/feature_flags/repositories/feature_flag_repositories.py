from typing import Sequence

from sqlmodel import Session, select

from app.api.feature_flags.domain.feature_flag_models import FeatureFlag


class FeatureFlagRepositorie:
    def __init__(self, session):
        self._session = session

    def add(self, entity: FeatureFlag):
        self._session.add(entity)

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

    @staticmethod
    def get_all(
        session: Session,
    ) -> Sequence[FeatureFlag] | Sequence[None]:
        return session.exec(select(FeatureFlag)).all()
