import abc
from typing import Generic, Sequence, TypeVar

T = TypeVar('T')


class AbstractRepository(Generic[T], abc.ABC):
    def __init__(self, session):
        self._session = session

    @abc.abstractmethod
    def add(self, obj) -> None:
        pass

    @abc.abstractmethod
    def get_by_id(self, identifier) -> T | None:
        pass

    @abc.abstractmethod
    def get_all(self) -> Sequence[T]:
        pass
