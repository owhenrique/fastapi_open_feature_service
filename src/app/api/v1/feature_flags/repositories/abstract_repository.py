import abc
from typing import Sequence
from uuid import UUID

from app.api.v1.feature_flags.domain.flag_model import Flag


class AbstractRepository(abc.ABC):
    def __init__(self, session):
        self._session = session

    @abc.abstractmethod
    def add(self, entity) -> None:
        pass

    @abc.abstractmethod
    def get_by_id(self, id: UUID) -> Flag | None:
        pass

    @abc.abstractmethod
    def get_all(self) -> Sequence[Flag]:
        pass
