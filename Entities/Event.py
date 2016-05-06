import datetime


class Event(object):
    eventID=0
    poiID=0
    startTime=datetime.datetime(2016,5,6,12,40,0)
    endTime=datetime.datetime(2016,5,6,12,40,0)
    prevEvent=0
    nextEvent=0

    def __init__(self,eventID,poiID,startTime,endTime,prevEvent,nextEvent):
        self.eventID=eventID
        self.poiID=poiID
        self.startTime=startTime
        self.endTime=endTime
        self.prevEvent=prevEvent
        self.nextEvent=nextEvent

    def printEvent(self):
        print("\n Event ID:%d" % self.eventID+"\n poi ID:%d" % self.poiID+"\n start time:" , self.startTime , "\n end time:" , self.endTime , "\n prev event:%d" % self.prevEvent+"\n next event:%d" % self.nextEvent)

#Test for print;
#event1=Event(1,1,startTime=datetime.datetime(2016,5,6,12,40,0),endTime=datetime.datetime(2016,5,6,12,40,0),prevEvent=0,nextEvent=2)
#event1.printEvent()