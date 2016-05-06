import datetime
class POI(object):
    poiID=0
    title="temp"
    description="temp"
    category="temp"
    geoLocation="Location"
    grade=1.01 #float
    cost=1.01 #float
    openingHour=datetime.datetime(2016,5,6,12,40,0)
    closingHour=datetime.datetime(2016,5,6,12,40,0)
    activityTime=0 #in minutes
    image="image"

    def __init__(self,poiID,title,description,category,geoLocation,grade,cost,openingHour,closingHour,activityTime,image):
        self.poiID=poiID
        self.title=title
        self.description=description
        self.category=category
        self.geoLocation=geoLocation
        self.grade=grade
        self.cost=cost
        self.openingHour=openingHour
        self.closingHour=closingHour
        self.activityTime=activityTime
        self.image=image
