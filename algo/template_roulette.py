import time
from Entities.Properties import Properties


class TemplateRoulette(object):

    def __init__(self, trip_type):
        self.trip_type = trip_type

    def generate_template(self):
        prop = Properties(dayBeginning=8.5, dayEnd=20.5, breakfastTime=9.0, lunchTime=13.0,
                          dinnerTime=19.0, type=self.trip_type)
        return prop
