import datetime


class POI(object):
    _poiID=0
    _title="temp"
    _description="temp"
    _category="temp"
    _grade=1.01 #float
    _openingHour=datetime.datetime(2016,5,6,12,40,0)
    _closingHour=datetime.datetime(2016,5,6,12,40,0)
    _activityTime=0 #in minutes
    _image="image"

    def __init__(self,poiID,title,description,category,geoLocation,grade,activityTime,image):
        self._poiID=poiID
        self._title=title
        self._description=description
        self._category=category
        self._geoLocation=geoLocation
        self._grade=grade
        self._activityTime=activityTime
        self._image=image

    def __str__(self):
        return 'ID: {} TITLE: {} DESC: {} CATEGORY: {} LOCATION: {} GRADE: {} ACTIVITY_TIME: {} IMAGE: {}'.format(
            self._poiID,self._title.encode('utf-8'),self._description.encode('utf-8'),self._category.encode('utf-8')
            ,self._geoLocation,self._grade,self._activityTime,
            self._image.encode('utf-8')
        )