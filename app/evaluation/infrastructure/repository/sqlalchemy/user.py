from evaluation.domain.user import User
from evaluation.domain.user_repository import UserMngRepository, UserFinderRepository
from sdk.adapter.sql.sqlalchemy import SqlAlchemyAdapter


class UserSqlMngRepository(UserMngRepository):
    def __init__(self, adapter: SqlAlchemyAdapter):
        self.__adapter = adapter
        self.__adapter._entity = User

    def persist(self, user: User) -> bool:
        return self.__adapter.persist(user)


class UserSqlFinderRepository(UserFinderRepository):
    def __init__(self, adapter: SqlAlchemyAdapter):
        self.__adapter = adapter
        self.__adapter._entity = User

    def find_by_id(self) -> User:
        return self.__adapter.find_all()
    
        
