import datetime
from DBHandler import DBHandler
from DBHandler import DBConnection


class POI(object):

    def __init__(self):
        self._title=""
        self._description=""
        self._category=""
        self._geoLocation=None
        self._grade=0.0
        self._activityTime=0
        self._image=""

    def __str__(self):
        return 'ID: {} TITLE: {} DESC: {} CATEGORY: {} LOCATION: {} GRADE: {} ACTIVITY_TIME: {} IMAGE: {}'.format(
            self._poiID,self._title.encode('utf-8'),self._description.encode('utf-8'),self._category.encode('utf-8')
            ,self._geoLocation,self._grade,self._activityTime,
            self._image.encode('utf-8')
        )

    def save_to_db(self):
        conn = DBConnection.DBConnection()
        handler = DBHandler.DBHandler(conn)
        return handler.create('poi','title,description,category,geoLocation,grade,activity_time,image',
                              "'{}','{}','{}','{}','{}','{}','{}'".format(self._title,self._description,
                                                                          self._category,
                                                     self._geoLocation,self._grade,self._activityTime,
                                                     self._image))
