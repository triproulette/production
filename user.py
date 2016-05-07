import falcon
import json
from DBHandler import DBHandler
from DBHandler import DBConnection


class Resource(object):

    def on_get(self, req, resp, action, id, fullname, avatar):

        if action == 'add':
            conn = DBConnection.DBConnection()
            handler = DBHandler.DBHandler(conn)
            user_id = handler.create(table_name='user',table_fields='id,name,avatar',table_values="'{}','{}','{}'"
                           .format(id,fullname,avatar))

            resp.body = '{msg: "success"}'
            resp.status = falcon.HTTP_200
