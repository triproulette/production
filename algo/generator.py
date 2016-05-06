import Entities.Entities

def getTrip(start, end, budget , properties ):
   trip = Entities.Trip()

   flight = Entities.POI()
   flight.category = "flight"
   flight.poiID=1
   flight.title="tlv->prague prg485"
   flight.description="flight from tlv to prague"
   flight.geoLocation="prague"
   flight.grade=1.01 #float
   flight.cost=1.01 #float
   flight.openingHour=datetime.datetime(2016,5,6,12,40,0)
   flight.closingHour=datetime.datetime(2016,5,6,12,40,0)
   flight.activityTime=3*60 #in minutes
   flight.image="image"

   ev1 = Entities.Event()
   ev1.eventID=2
   ev1.poiID=1
   ev1.startTime=datetime.datetime(2016,5,6,12,40,0)
   ev1.endTime=datetime.datetime(2016,5,6,12,40,0)
   ev1.prevEvent=0
   ev1.nextEvent=0

   trip.start = 2
   trip.end =
   return trip


