from evaluation.application.bus.user_command_query import UpdateUserCommand, CreateUserCommand, FindUserQuery
from evaluation.domain.user import UserFactory, UserName
from evaluation.domain.user_repository import UserFinderRepository, UserMngRepository
from evaluation.domain.user_service import UserFinderService


class UserFinderdAppService:
    def __init__(self, user_finder_repository: UserFinderRepository):
        self.user_finder_repository = user_finder_repository

    def find_by_id(self):
        user = self.user_finder_repository.find_by_id()
        data = {}
        for us in user:
            data[us.id]={
                'name': us.name,
                'nota': us.nota
            }      
        return data

class UserCreateAppService:
    def __init__(self, user_mng_repository: UserMngRepository):
        self.user_mng_repository = user_mng_repository

    def create(self, id, name, nota):
        nota = UserFactory.create(id, name, nota)
        self.user_mng_repository.persist(nota)
        return True
