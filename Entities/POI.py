import datetime
class POI(object):
    _poiID=0
    _title="temp"
    _description="temp"
    _category="temp"
    _geoLocation="Location"
    _grade=1.01 #float
    _cost=1.01 #float
    _openingHour=datetime.datetime(2016,5,6,12,40,0)
    _closingHour=datetime.datetime(2016,5,6,12,40,0)
    _activityTime=0 #in minutes
    _image="image"

    def __init__(self,poiID,title,description,category,geoLocation,grade,cost,openingHour,closingHour,activityTime,image):
        self._poiID=poiID
        self._title=title
        self._description=description
        self._category=category
        self._geoLocation=geoLocation
        self._grade=grade
        self._cost=cost
        self._openingHour=openingHour
        self._closingHour=closingHour
        self._activityTime=activityTime
        self._image=image
