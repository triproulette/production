from Entities.Event import Event
import datetime
from DBHandler import DBHandler
from DBHandler import DBConnection


class Trip(object):

    def __init__(self, user_id):
        self._user_id = user_id
        self._eventList = []

    def setEventList(self,index,newEvent):
        self._eventList.insert(index,newEvent)

    def printTrip(self):
        print("\n Trip ID:%d" % self._tripID+"\n Budget:%d" % self._budget)
        #   printing event list:
        for event in self._eventList:
            event.printEvent()

    def updateEventList(self,event):
        listSize=len(self._eventList)
        lastEvent=self._eventList[listSize-1]
        del self._eventList[listSize-1]
        self._eventList.insert(listSize-1,event)
        self._eventList.insert(listSize,lastEvent)

    def getLastEvent(self):
        listSize=len(self._eventList)
        return self._eventList[listSize-1]

    def getOneBeforeLastEvent(self):
        listSize = len(self._eventList)
        return self._eventList[listSize - 2]
    #

    def save_to_db(self):
        conn = DBConnection.DBConnection()
        handler = DBHandler.DBHandler(conn)
        return handler.create(table_name='trip', table_fields='user_id', table_values="'{}'".format(self._user_id))
