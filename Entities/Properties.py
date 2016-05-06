from time import time


class Properties(object):

    def __init__(self, tripID, dayBeginning, dayEnd, breakfastTime, lunchTime, dinnerTime, type):
        self._tripID = tripID
        self._dayBeginning = dayBeginning
        self._dayEnd = dayEnd
        self._breakfastTime = breakfastTime
        self._lunchTime = lunchTime
        self._dinnerTime = dinnerTime
        self._type = type
