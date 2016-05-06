import Entities.Imports

def getTrip(start, end, budget , properties ):

   ##stub
   trip = Entities.Trip()

   flight = Entities.POI()
   flight.category = "flight"
   flight.poiID=1
   flight.title="tlv->prague prg485"
   flight.description="flight from tlv to prague"
   flight.geoLocation="prague"
   flight.grade=1.01 #float
   flight.cost=1.01 #float
   flight.openingHour=datetime.datetime(2016,5,6,5,40,0)
   flight.closingHour=datetime.datetime(2016,5,6,8,40,0)
   flight.activityTime=3*60 #in minutes
   flight.image="image"


   ev1 = Entities.Event()
   ev1.eventID=2
   ev1.poiID=1
   ev1.startTime = datetime.datetime(2016,5,6,8,40,0)
   ev1.endTime = datetime.datetime(2016,5,6,11,40,0)
   ev1.prevEvent=0
   ev1.nextEvent=2

   poi = Entities.POI()
   poi.category = "flight"
   poi.poiID = 3
   poi.title = "some event"
   poi.description = "some desription about some event"
   poi.geoLocation = "10.10,20.20"
   poi.grade = 1.01  # float
   poi.cost = 1.01  # float
   poi.openingHour = datetime.datetime(2016, 5, 6, 12, 40, 0)
   poi.closingHour = datetime.datetime(2016, 5, 6, 12, 40, 0)
   poi.activityTime = 3 * 60  # in minutes
   poi.image = "image"


   ev2 = ev1
   ev2.eventID  = 4
   ev2.poiID=3
   ev2.startTime=datetime.datetime(2016,5,6,12,40,0)
   ev2.endTime=datetime.datetime(2016,5,6,12,40,0)

   ev3 = ev1
   ev3.eventID  = 4
   ev3.poiID=3

   flight2 = flight
   flight2.poiID = 5
   flight.title = "prague->tlv tlv2425"
   flight.description = "flight from prague to tlv"
   flight.geoLocation = "tlv"
   flight.grade = 1.01  # float
   flight.cost = 1.01  # float
   flight.openingHour = datetime.datetime(2016, 5, 6, 20, 40, 0)
   flight.closingHour = datetime.datetime(2016, 5, 6, 23, 40, 0)
   flight.activityTime = 3 * 60  # in minutes
   flight.image = "image"


   trip.start = 2
   trip.end = 5
   return trip



}

