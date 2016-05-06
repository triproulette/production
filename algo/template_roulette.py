from time import time
from Entities.Properties import Properties


class TemplateRoulette(object):

    def __init__(self, trip_type):
        self.trip_type = trip_type

    def generate_template(self):
        prop = Properties(dayBeginning=time(8,0,0),dayEnd=time(20,0,0),breakfastTime=time(9,0,0),lunchTime=time(13,0,0),
                          dinnerTime=time(19,0,0),type=self.trip_type)
        return prop
