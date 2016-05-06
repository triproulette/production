import datetime
class Properties(object):
    _tripID=0
    _dayBeginning=datetime.datetime(2016,5,6,12,40,0)
    _dayEnd=datetime.datetime(2016,5,6,12,40,0)
    _breakfastTime=datetime.datetime(2016,5,6,12,40,0)
    _lunchTime=datetime.datetime(2016,5,6,12,40,0)
    _dinnerTime=datetime.datetime(2016,5,6,12,40,0)
    _type="temp" #nightlife,history,coaster,nature

    def __init__(self,tripID,dayBeginning,dayEnd,breakfastTime,lunchTime,dinnerTime,type):
        self._tripID=tripID
        self._dayBeginning=dayBeginning
        self._dayEnd=dayEnd
        self._breakfastTime=breakfastTime
        self._lunchTime=lunchTime
        self._dinnerTime=dinnerTime
        self._type=type