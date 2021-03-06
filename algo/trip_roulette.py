from algo.template_roulette import TemplateRoulette
from Entities.Trip import Trip
from Entities.Event import Event
from Entities.POI import POI
from Entities.GeoLocation import GeoLocation
from datetime import datetime
from datetime import timedelta
from algo.step_generator import stepGenerator


class TripRoulette(object):

    def __init__(self, trip_type, city, start_trip, end_trip):
        self.trip_type = trip_type
        self.city = city
        self.start_trip = start_trip
        self.end_trip = end_trip

    def generate_random_trip(self, user_id):
        self._prop = TemplateRoulette(self.trip_type).generate_template()   # generate template
        self._trip = Trip(user_id)  # generate trip entity
        poi = POI()
        poi._title="flight"
        poi._description="flight"
        poi._category="flight"
        poi._geoLocation=GeoLocation(49.009677, 2.547903)
        self._trip._eventList.append(Event(
                                           startTime=self.start_trip,
                                           endTime=self.start_trip,
                                           poiID=poi.save_to_db()))     # append first event
        # amsterdam airport: 52.310558, 4.768221
        # paris laptop: 49.009677, 2.547903
        self._trip._eventList.append(Event(
                                           startTime=self.end_trip,
                                           endTime=self.end_trip,
                                           poiID=poi.save_to_db()))    # append last event

        while abs(self._trip.getOneBeforeLastEvent()._endTime-self._trip.getLastEvent()._startTime) > timedelta(days=0, hours=2, minutes=0, seconds=0, microseconds=0) :
            stepGenerator(self._prop, self._trip.getOneBeforeLastEvent())
        self._trip.save_to_db()
        return self._trip