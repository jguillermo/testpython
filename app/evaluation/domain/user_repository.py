from abc import ABC, abstractmethod
from evaluation.domain.user import User


class UserMngRepository(ABC):
    @abstractmethod
    def persist(self, user: User) -> bool:
        pass


class UserFinderRepository(ABC):
    @abstractmethod
    def find_by_id(self) -> User:
        pass


class UserSearchRepository(ABC):
    @abstractmethod
    def listAll(self, filter):
        pass
