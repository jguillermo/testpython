from sdk.types import TypeUuid, TypeString, TypeBase


class UserId(TypeUuid):
    pass


class UserName(TypeString):

    def validate(self):
        super().validate()
        if self._value.__len__() < 3:
            raise Exception("El nombre debe ser mayor a 2 caracteres")


class UserNota(TypeString):
    pass


class User:
    def __init__(self, id, name, nota):
        self.id = id
        self.name = name
        self.nota = nota


class UserFactory:
    @staticmethod
    def create(id,name,nota) -> User:
        id = UserId(id)
        name = UserName(name)
        nota = UserNota(nota)
        UserFactory._validate([id, name, nota])
        return User(id.value(), name.value(), nota.value())

    @staticmethod
    def _validate(value_object):
        for vo in value_object:  # type: TypeBase
            vo.validate()
