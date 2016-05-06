import falcon
from DBHandler import DBHandler
from DBHandler import DBConnection
from Entities.POI import POI
import datetime


class Resource(object):

    def on_get(self, req, resp):
        conn = DBConnection.DBConnection()
        handler = DBHandler.DBHandler(conn)
        #tripId = handler.create(table_name='trip', table_fields='user_id', table_values="'some_user_id'")
        poi = POI()
        poi.category = "flight"
        poi.title = "some event"
        poi.description = "some desription about some event"
        poi.geoLocation = "10.10,20.20"
        poi.grade = 1.01  # float
        poi.activityTime = 3 * 60  # in minutes
        poi.image = "image"
        poiId = poi.save_to_db()
        resp.body = '{"message": "poi inserted, id is %s"}' % poiId
        resp.status = falcon.HTTP_200
#sandak
#Tomer
#bar
#asaf