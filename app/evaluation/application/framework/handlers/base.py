# -*- coding: utf-8 -*-

from evaluation.infrastructure.bus import CommandBusSync, QueryBusSync
import jwt


class Base:

    def __init__(self) -> None:
        self.command_bus = CommandBusSync()
        self.command_query = QueryBusSync()

    def auth(self,token):
        encoded_jwt = jwt.encode({'key': '123'}, 'secret', algorithm='HS256')
        print ('*******************')
        print (encoded_jwt)
        print ('******************')

        try:
            jwt.decode(
                token,
                'secret', algorithms=['HS256'])

        except Exception as e:
            raise Exception('error de autenticacion')
