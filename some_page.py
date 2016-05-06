import falcon
from DBHandler import DBHandler
from DBHandler import DBConnection


class Resource(object):

    def on_get(self, req, resp):
        conn = DBConnection.DBConnection()
        handler = DBHandler.DBHandler(conn)
        tripId = handler.create(table_name='trip',table_fields='user_id',table_values="'some_user_id'")
        resp.body = '{"message": "trip inserted, id is {}"}'.format(tripId)
        resp.status = falcon.HTTP_200
#sandak
#Tomer
#bar
#asaf