from typing import Sequence
from uuid import UUID

from sqlmodel import Session, or_, select

from app.api.feature_flags.domain.flag_model import Flag
from app.api.feature_flags.repositories.abstract_repositorie import (
    AbstractRepositorie,
)


class FlagRepositorie(AbstractRepositorie):
    def __init__(self, session: Session):
        super().__init__(session)

    def add(self, entity: Flag) -> None:
        self._session.add(entity)

    def get_by_id(self, id: UUID) -> Flag | None:
        return self._session.exec(select(Flag).where(Flag.id == id)).first()

    def get_by_name(self, name: str) -> Flag | None:
        return self._session.exec(
            select(Flag).where(Flag.name == name)
        ).first()

    def get_by_technical_key(self, technical_key: str) -> Flag | None:
        return self._session.exec(
            select(Flag).where(Flag.technical_key == technical_key)
        ).first()

    def get_by_name_or_technical_key(
        self, name=None, technical_key=None
    ) -> Flag | None:
        return self._session.exec(
            select(Flag).where(
                or_(
                    Flag.name == name,
                    Flag.technical_key == technical_key,
                )
            )
        ).first()

    def get_all(self) -> Sequence[Flag]:
        return self._session.exec(select(Flag)).all()

    def delete(self, entity: Flag) -> None:
        self._session.delete(entity)
