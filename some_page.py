import falcon
from DBHandler import DBHandler
from DBHandler import DBConnection
from Entities.POI import POI
from Entities.Trip import Trip
from Entities.Event import Event
import datetime


class Resource(object):

    def on_get(self, req, resp):
        """
        conn = DBConnection.DBConnection()
        handler = DBHandler.DBHandler(conn)
        trip = Trip(user_id='FUCKING_FB_ID')
        #tripId = trip.save_to_db()
        poi = POI(category="flight",title="some poi",description="some desc",geoLocation="10.2,11.1",
                  grade=1.11,activityTime=3,image="blalala.png")
        #poiId = poi.save_to_db()
        event = Event(poiID=1,startTime=datetime.datetime(2016,5,6,12,40,0),endTime=datetime.datetime(2016,5,6,12,40,0))
        eventId = event.save_to_db()
        #resp.body = '{"poi": "poi inserted, id is %s", "trip": "trip id inserted id %s"}' % (poiId, tripId)
        resp.body = '{"event: %s"}' % (eventId)
        resp.status = falcon.HTTP_200
        """