import falcon
from DBHandler import DBHandler
from DBHandler import DBConnection
from Entities.POI import POI
from Entities.Trip import Trip


class Resource(object):

    def on_get(self, req, resp):
        conn = DBConnection.DBConnection()
        handler = DBHandler.DBHandler(conn)
        trip = Trip(user_id='FUCKING_FB_ID')
        tripId = trip.save_to_db()
        poi = POI(category="flight",title="some poi",description="some desc",geoLocation="10.2,11.1",
                  grade=1.11,activityTime=3,image="blalala.png")
        poiId = poi.save_to_db()
        resp.body = '{"poi": "poi inserted, id is %s", "trip": "trip id inserted id %s"}' % (poiId, tripId)
        resp.status = falcon.HTTP_200