import abc
from typing import Generic, Sequence, TypeVar

T = TypeVar('T')


class AbstractService(Generic[T], abc.ABC):
    def __init__(self, repository):
        self._repository = repository

    @abc.abstractmethod
    def create(self, obj) -> T:
        pass

    @abc.abstractmethod
    def read_all(self) -> Sequence[T]:
        pass

    @abc.abstractmethod
    def read_one(self, identifier) -> T:
        pass

    @abc.abstractmethod
    def update(self, identifier, obj) -> T:
        pass

    @abc.abstractmethod
    def delete(self, identifier) -> None:
        pass
