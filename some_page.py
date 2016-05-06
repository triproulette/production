import falcon
from DBHandler import DBHandler
from DBHandler import DBConnection
from Entities.POI import POI


class Resource(object):

    def on_get(self, req, resp):
        conn = DBConnection.DBConnection()
        handler = DBHandler.DBHandler(conn)
        #tripId = handler.create(table_name='trip', table_fields='user_id', table_values="'some_user_id'")
        poi = POI(category="flight",title="some poi",description="some desc",geoLocation="10.2,11.1",
                  grade=1.11,activityTime=3,image="blalala.png")
        poiId = poi.save_to_db()
        resp.body = '{"message": "poi inserted, id is %s"}' % poiId
        resp.status = falcon.HTTP_200