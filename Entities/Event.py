import datetime
from DBHandler import DBHandler
from DBHandler import DBConnection


class Event(object):

    def __init__(self,poiID,startTime,endTime):
        self._poiID=poiID
        self._startTime=startTime
        self._endTime=endTime

    def printEvent(self):
        print("\n Eventt ID:%d" % self._eventID+"\n poi ID:%d" % self._poiID+"\n start time:" , self._startTime , "\n end time:" , self._endTime, "\n **************")

    def save_to_db(self):
        conn = DBConnection.DBConnection()
        handler = DBHandler.DBHandler(conn)
        return handler.create('event','poi_id,s_time,e_time',
                              "'{}','{}','{}'".format(self._poiID,self._startTime,self._endTime))

#Test for print;
#event1=Event(1,1,startTime=datetime.datetime(2016,5,6,12,40,0),endTime=datetime.datetime(2016,5,6,12,40,0))
#event1.printEvent()