import datetime


class Event(object):

    def __init__(self,eventID,poiID,startTime,endTime):
        self._eventID=eventID
        self._poiID=poiID
        self._startTime=startTime
        self._endTime=endTime

    def printEvent(self):
        print("\n Event ID:%d" % self._eventID+"\n poi ID:%d" % self._poiID+"\n start time:" , self._startTime , "\n end time:" , self._endTime, "\n **************")

#Test for print;
#event1=Event(1,1,startTime=datetime.datetime(2016,5,6,12,40,0),endTime=datetime.datetime(2016,5,6,12,40,0))
#event1.printEvent()