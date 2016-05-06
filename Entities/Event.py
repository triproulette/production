import datetime


class Event(object):
    _eventID=0
    _poiID=0
    _startTime=datetime.datetime(2016,5,6,12,40,0)
    _endTime=datetime.datetime(2016,5,6,12,40,0)
    _prevEvent=0
    _nextEvent=0

    def __init__(self,eventID,poiID,startTime,endTime,prevEvent,nextEvent):
        self._eventID=eventID
        self._poiID=poiID
        self._startTime=startTime
        self._endTime=endTime
        self._prevEvent=prevEvent
        self._nextEvent=nextEvent

    def printEvent(self):
        print("\n Event ID:%d" % self._eventID+"\n poi ID:%d" % self._poiID+"\n start time:" , self._startTime , "\n end time:" , self._endTime , "\n prev event:%d" % self._prevEvent+"\n next event:%d" % self._nextEvent)

#Test for print;
#event1=Event(1,1,startTime=datetime.datetime(2016,5,6,12,40,0),endTime=datetime.datetime(2016,5,6,12,40,0),prevEvent=0,nextEvent=2)
#event1.printEvent()