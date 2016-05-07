from Entities.Event import Event
import datetime


class Trip(object):
    _tripID=0
    _start=0 # event id
    _end=0 # event id
    _budget=0
    #_evenList=[]

    def __init__(self,tripID,start,end,budget):
        self._tripID=tripID
        self._start=start
        self._end=end
        self._budget=budget
        self._eventList=[]

    def setEventList(self,index,newEvent):
        self._eventList.insert(index,newEvent)

    def printTrip(self):
        print("\n Trip ID:%d" % self._tripID+"\n Budget:%d" % self._budget)
        #printing event list:
        i=0
        for event in self._eventList:
            event.printEvent()

    def updateEventList(self,event):
        listSize=len(self._eventList)
        lastEvent=self._eventList[listSize-1]
        del self._eventList[listSize-1]
        self._eventList.insert(listSize-1,event)
        self._eventList.insert(listSize,lastEvent)

#Testing of setEventList with int List; Works by index :)
Trip1=Trip(1,9,9,500)
Trip1.setEventList(0,Event(2,3,startTime=datetime.datetime(2016,5,6,12,40,0),endTime=datetime.datetime(2016,5,6,12,40,0)))
Trip1.printTrip()
event1= Event(3,54,startTime=datetime.datetime(2016,5,6,12,45,35),endTime=datetime.datetime(2016,5,6,12,46,44))
Trip1.updateEventList(event1)
Trip1.printTrip()