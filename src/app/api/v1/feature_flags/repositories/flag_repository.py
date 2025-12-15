from typing import Sequence
from uuid import UUID

from sqlmodel import or_, select

from app.api.v1.feature_flags.deps.session_dependency import SessionDep
from app.api.v1.feature_flags.domain.flag_model import Flag
from app.api.v1.feature_flags.repositories.abstract_repository import (
    AbstractRepository,
)


class FlagRepository(AbstractRepository):
    def __init__(self, session: SessionDep):
        super().__init__(session)

    def add(self, entity: Flag) -> None:
        self._session.add(entity)
        self._session.commit()
        self._session.refresh(entity)

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

    def get_all(self) -> Sequence[Flag]:
        return self._session.exec(select(Flag)).all()

    def update(self, entity: Flag) -> None:
        self._session.add(entity)
        self._session.commit()
        self._session.refresh(entity)

    def delete(self, entity: Flag) -> None:
        self._session.delete(entity)
        self._session.commit()
