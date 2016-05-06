from algo.template_roulette import TemplateRoulette


class TripRoulette(object):

    def __init__(self, trip_type):
        self.trip_type = trip_type

    def generate_random_trip(self):
        self.prop = TemplateRoulette(self.trip_type).generate_template()


trip = TripRoulette(trip_type="Travel")
trip.generate_random_trip()
print trip.prop