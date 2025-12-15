import abc
from typing import Sequence

from app.api.v1.feature_flags.domain.flag_model import Flag


class AbstractService(abc.ABC):
    def __init__(self, repository):
        self._repository = repository

    @abc.abstractmethod
    def create(self, flag) -> Flag:
        pass

    @abc.abstractmethod
    def read_all(self) -> Sequence[Flag]:
        pass

    @abc.abstractmethod
    def read_one(self, technical_key) -> Flag:
        pass

    @abc.abstractmethod
    def update(self, technical_key, flag) -> Flag:
        pass

    @abc.abstractmethod
    def delete(self, technical_key) -> None:
        pass
