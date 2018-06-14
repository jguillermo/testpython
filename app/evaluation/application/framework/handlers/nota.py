# -*- coding: utf-8 -*-
import falcon

from evaluation.application.bus.user_command_query import CreateUserCommand, UpdateUserCommand, FindUserQuery
from evaluation.application.framework.decorators.service import handler_except
from evaluation.application.framework.handlers.base import Base
from sdk.types import TypeUuid

class NotaHandler(Base):

    @handler_except
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        self.auth(req.media.get('token', ''))
        id = TypeUuid.random().value()
        command = CreateUserCommand(
            id=id,
            name=req.media.get('name', ''),
            nota=req.media.get('nota', ''))
        self.command_bus.dispatch(command)
        return {'id': id}

    @handler_except
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        self.auth(req.params.__getitem__('token'))
        query = FindUserQuery('1')
        return self.command_query.ask(query)

