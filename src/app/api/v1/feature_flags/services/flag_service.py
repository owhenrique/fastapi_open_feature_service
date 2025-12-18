from typing import Sequence

from pydantic import ValidationError

from app.api.v1.feature_flags.deps.repository_dependency import RepositoryDep
from app.api.v1.feature_flags.domain.flag_context_model import FlagContext
from app.api.v1.feature_flags.domain.flag_model import (
    Flag,
    OperationalStatusEnum,
)
from app.api.v1.feature_flags.exceptions.flag_exceptions import (
    FlagContextValidationException,
    FlagNameAlreadyExistsException,
    FlagNotFoundException,
    FlagTechnicalKeyAlreadyExistsException,
)
from app.api.v1.feature_flags.schemas.flag_schemas import (
    FlagCreateSchema,
    FlagUpdateSchema,
)
from app.core.abstract_service import AbstractService


class FlagService(AbstractService):
    def __init__(self, repository: RepositoryDep):
        super().__init__(repository)

    def create(self, obj: FlagCreateSchema) -> Flag:
        # Todo: change featureflagcreateschema to feature flag entity/model
        # decloupling
        if self._repository.get_by_name(obj.name) is not None:
            raise FlagNameAlreadyExistsException

        if (
            self._repository.get_by_technical_key(obj.technical_key)
            is not None
        ):
            raise FlagTechnicalKeyAlreadyExistsException

        instance = Flag(
            name=obj.name,
            technical_key=obj.technical_key,
            operational_status=obj.operational_status,
        )

        self._repository.add(instance)

        return instance

    def read_all(self) -> Sequence[Flag]:
        return self._repository.get_all()

    def read_one(self, identifier: str) -> Flag:
        instance = self._repository.get_by_technical_key(identifier)

        if instance is None:
            raise FlagNotFoundException

        return instance

    def update(self, identifier: str, obj: FlagUpdateSchema) -> Flag:
        instance = self._repository.get_by_technical_key(identifier)

        if instance is None:
            raise FlagNotFoundException

        if obj.name:
            db_flag = self._repository.get_by_name(obj.name)

            if db_flag and db_flag.id is not instance.id:
                raise FlagNameAlreadyExistsException

            instance.name = obj.name

        if obj.technical_key:
            db_flag = self._repository.get_by_technical_key(obj.technical_key)

            if db_flag and db_flag.id is not instance.id:
                raise FlagTechnicalKeyAlreadyExistsException

            instance.technical_key = obj.technical_key

        if obj.operational_status:
            instance.operational_status = obj.operational_status

        self._repository.update(instance)

        return instance

    def delete(self, identifier: str) -> None:
        instance = self._repository.get_by_technical_key(identifier)

        if instance is None:
            raise FlagNotFoundException

        self._repository.delete(instance)

    def is_enabled(self, identifier: str) -> bool:
        instance = self._repository.get_by_technical_key(identifier)

        if instance is None:
            raise FlagNotFoundException

        if instance.operational_status is not OperationalStatusEnum.ON:
            return False

        return True

    def is_enabled_with_context(
        self, identifier: str, environment: str, actor: str
    ) -> bool:
        instance = self._repository.get_by_technical_key(identifier)

        context_data = {'environment': environment, 'actor': actor}

        try:
            context = FlagContext.model_validate(context_data)  # noqa: F841
        except ValidationError:
            raise FlagContextValidationException

        if instance is None:
            raise FlagNotFoundException

        if instance.operational_status is not OperationalStatusEnum.ON:
            return False

        return True
