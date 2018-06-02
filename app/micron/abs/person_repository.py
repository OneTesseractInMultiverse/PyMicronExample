from abc import (
    ABCMeta,
    abstractmethod
)


class AbsPersonRepository(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, personal_id: str) -> dict or None:
        pass

    @abstractmethod
    def create(self, person_state: dict) -> bool:
        pass