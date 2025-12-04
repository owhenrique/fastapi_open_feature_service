from typing import Sequence

from sqlmodel import Session, select

from app.api.feature_flags.domain.feature_flag_models import FeatureFlag


class FeatureFlagRepositorie:
    @staticmethod
    def add(session: Session, entity: FeatureFlag):
        session.add(entity)

    @staticmethod
    def get_by_name(session: Session, name: str) -> FeatureFlag | None:
        instance = session.exec(
            select(FeatureFlag).where(FeatureFlag.name == name)
        ).first()

        return instance

    @staticmethod
    def get_by_technical_key(
        session: Session, technical_key: str
    ) -> FeatureFlag | None:
        return session.exec(
            select(FeatureFlag).where(
                FeatureFlag.technical_key == technical_key
            )
        ).first()

    @staticmethod
    def get_all(
        session: Session,
    ) -> Sequence[FeatureFlag] | Sequence[None]:
        return session.exec(select(FeatureFlag)).all()
