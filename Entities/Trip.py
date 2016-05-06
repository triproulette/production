from Entities.Event import Event
import datetime


class Trip(object):
    tripID=0
    start=0 # event id
    end=0 # event id
    budget=0
    eventList= []

    def __init__(self,tripID,start,end,budget):
        self.tripID=tripID
        self.start=start
        self.end=end
        self.budget=budget
        self.eventList

    def setEventList(self,index,newEvent):
        self.eventList.insert(index,newEvent)

    def printTrip(self):
        print("\n Trip ID:%d" % self.tripID+"\n Budget:%d" % self.budget)
        #printing event list:
        i=0
        for event in self.eventList:
            event.printEvent()


#Testing of setEventList with int List; Works by index :)
Trip1=Trip(1,9,9,500)
Trip1.setEventList(0,Event(2,3,startTime=datetime.datetime(2016,5,6,12,40,0),endTime=datetime.datetime(2016,5,6,12,40,0),prevEvent=2,nextEvent=3))
print(Trip1.printTrip())