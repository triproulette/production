from algo.template_roulette import TemplateRoulette
from Entities.Trip import Trip
from Entities.Event import Event
from datetime import datetime
import step_generator


class TripRoulette(object):

    def __init__(self, trip_type, city, start_trip, end_trip):
        self.trip_type = trip_type
        self.city = city
        self.start_trip = start_trip
        self.end_trip = end_trip

    def generate_random_trip(self):
        self._prop = TemplateRoulette(self.trip_type).generate_template()   # generate template
        self._trip = Trip(tripID=0)  # generate trip entity
        self._trip._eventList.append(Event(eventID=0,
                                           startTime=datetime(self.start_trip),
                                           endTime=datetime(self.start_trip),
                                           poiID=0))     # append first event
        self._trip._eventList.append(Event(eventID=99,
                                           startTime=datetime(self.end_trip),
                                           endTime=datetime(self.end_trip),
                                           poiID=1))    # append last event

        whule
        stepGenerator(prop, prevnt)