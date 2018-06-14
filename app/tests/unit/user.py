import unittest
from unittest import mock

from evaluation.application.bus.user_command_query import FindUserQuery, CreateUserCommand, UpdateUserCommand
from evaluation.application.services.user_app_service import UserFinderdAppService, UserCreateAppService
from evaluation.domain.user import User
from evaluation.domain.user_repository import UserFinderRepository, UserMngRepository
from sdk.exception import RepositoryNotFound


class UserMockRepository:
    @staticmethod
    def finder_ok():
        repository = mock.create_autospec(UserFinderRepository)
        repository.find_by_id.return_value = User('123', 'jose', 'guillermo')
        return repository

    @staticmethod
    def finder_error():
        repository = mock.create_autospec(UserFinderRepository)
        repository.find_by_id.return_value = None
        return repository

    @staticmethod
    def mng_ok():
        repository = mock.create_autospec(UserMngRepository)
        repository.persist.return_value = True
        return repository


class TestUserFinderService(unittest.TestCase):

    def test_user_find_by_id_ok(self):
        service = UserFinderdAppService(UserMockRepository.finder_ok())
        user = service.find_by_id('123')
        self.assertEqual('123', user['id'])

    def test_user_find_by_id_error(self):
        service = UserFinderdAppService(UserMockRepository.finder_error())
        with self.assertRaises(RepositoryNotFound):
            service.find_by_id('123')


class TestUserCreateService(unittest.TestCase):

    def test_user_create_ok(self):
        service = UserCreateAppService(UserMockRepository.mng_ok())
        status = service.create('123', 'jose', 'guillermo')
        self.assertEqual(True, status)




