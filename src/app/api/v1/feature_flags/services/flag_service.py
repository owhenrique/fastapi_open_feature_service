from typing import Sequence

from sqlmodel import Session

from app.api.v1.feature_flags.domain.flag_model import Flag
from app.api.v1.feature_flags.exceptions.flag_exceptions import (
    FlagNameAlreadyExistsException,
    FlagNotFoundException,
    FlagTechnicalKeyAlreadyExistsException,
)
from app.api.v1.feature_flags.repositories.flag_repositorie import (
    FlagRepositorie,
)
from app.api.v1.feature_flags.schemas.flag_schemas import (
    FlagCreateSchema,
    FlagUpdateSchema,
)
from app.api.v1.feature_flags.services.abstract_service import AbstractService


class FlagService(AbstractService):
    def __init__(self, session: Session):
        super().__init__(session, FlagRepositorie(session))

    def create(self, flag: FlagCreateSchema) -> Flag:
        # Todo: change featureflagcreateschema to feature flag entity/model
        # decloupling
        if self._repositorie.get_by_name(flag.name) is not None:
            raise FlagNameAlreadyExistsException

        if (
            self._repositorie.get_by_technical_key(flag.technical_key)
            is not None
        ):
            raise FlagTechnicalKeyAlreadyExistsException

        instance = Flag(
            name=flag.name,
            technical_key=flag.technical_key,
            operational_status=flag.operational_status,
        )

        self._repositorie.add(instance)
        self._session.commit()
        self._session.refresh(instance)

        return instance

    def read_all(self) -> Sequence[Flag]:
        return self._repositorie.get_all()

    def read_one(self, technical_key: str) -> Flag:
        instance = self._repositorie.get_by_technical_key(technical_key)

        if instance is None:
            raise FlagNotFoundException

        return instance

    def update(self, technical_key: str, flag: FlagUpdateSchema) -> Flag:
        instance = self._repositorie.get_by_technical_key(technical_key)

        if instance is None:
            raise FlagNotFoundException

        if flag.name:
            db_flag = self._repositorie.get_by_name(flag.name)

            if db_flag and db_flag.id is not instance.id:
                raise FlagNameAlreadyExistsException

            instance.name = flag.name

        if flag.technical_key:
            db_flag = self._repositorie.get_by_technical_key(
                flag.technical_key
            )

            if db_flag and db_flag.id is not instance.id:
                raise FlagTechnicalKeyAlreadyExistsException

            instance.technical_key = flag.technical_key

        if flag.operational_status:
            instance.operational_status = flag.operational_status

        self._session.commit()
        self._session.refresh(instance)

        return instance

    def delete(self, technical_key: str) -> None:
        instance = self._repositorie.get_by_technical_key(technical_key)

        if instance is None:
            raise FlagNotFoundException

        self._repositorie.delete(instance)
        self._session.commit()
