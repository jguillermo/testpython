from sdk.bus import Command, Query


class FindUserQuery(Query):
    def __init__(self, id):
        self.id = id


class CreateUserCommand(Command):
    def __init__(self, id, name, nota):
        self.id = id
        self.name = name
        self.nota = nota


class UpdateUserCommand(Command):
    def __init__(self, id, name, nota):
        self.id = id
        self.name = name
        self.nota = nota
