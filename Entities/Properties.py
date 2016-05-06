import time
class Properties(object):
    _tripID=0
    _dayBeginning=time.time(8,0,0)
    _dayEnd=time.time(20,0,0)
    _breakfastTime=time.time(9,0,0)
    _lunchTime=time.time(12,30,0)
    _dinnerTime=time.time(19,00,0)
    _type="temp" #nightlife,history,coaster,nature

    def __init__(self,tripID,dayBeginning,dayEnd,breakfastTime,lunchTime,dinnerTime,type):
        self._tripID=tripID
        self._dayBeginning=dayBeginning
        self._dayEnd=dayEnd
        self._breakfastTime=breakfastTime
        self._lunchTime=lunchTime
        self._dinnerTime=dinnerTime
        self._type=type