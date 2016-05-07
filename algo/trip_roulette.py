from algo.template_roulette import TemplateRoulette
from Entities.Trip import Trip
from Entities.Event import Event
from Entities.POI import POI
from Entities.GeoLocation import GeoLocation
from datetime import datetime
from algo.step_generator import stepGenerator



class TripRoulette(object):

    def __init__(self, trip_type, city, start_trip, end_trip):
        self.trip_type = trip_type
        self.city = city
        self.start_trip = start_trip
        self.end_trip = end_trip

    def generate_random_trip(self):
        self._prop = TemplateRoulette(self.trip_type).generate_template()   # generate template
        self._trip = Trip(tripID=0)  # generate trip entity
        poi = POI()
        poi._title="flight"
        poi._description="flight"
        poi._category="flight"
        poi._geoLocation=GeoLocation(49.009677, 2.547903)
        poi._trip._eventList.append(Event(eventID=0,
                                           startTime=datetime(self.start_trip),
                                           endTime=datetime(self.start_trip),
                                           poiID=poi.save_to_db()))     # append first event
        # amsterdam airport: 52.310558, 4.768221
        # paris laptop: 49.009677, 2.547903
        self._trip._eventList.append(Event(eventID=99,
                                           startTime=datetime(self.end_trip),
                                           endTime=datetime(self.end_trip),
                                           poiID=poi.save_to_db()))    # append last event

        while  abs(self._trip.getOneBeforeLastEvent()._endTime-self._trip.getLastEvent()._startTime) > datetime.timedelta(days=0, hours=2, minutes=0, seconds=0, microseconds=0) :
            stepGenerator(self._prop, self._trip.getOneBeforeLastEvent())

        return self._trip