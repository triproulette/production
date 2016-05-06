import datetime
class Properties(object):
    tripID=0
    dayBeginning=datetime.datetime(2016,5,6,12,40,0)
    dayEnd=datetime.datetime(2016,5,6,12,40,0)
    breakfastTime=datetime.datetime(2016,5,6,12,40,0)
    lunchTime=datetime.datetime(2016,5,6,12,40,0)
    dinnerTime=datetime.datetime(2016,5,6,12,40,0)
    type="temp" #nightlife,history,coaster,nature

    def __init__(self,tripID,dayBeginning,dayEnd,breakfastTime,lunchTime,dinnerTime,type):
        self.tripID=tripID
        self.dayBeginning=dayBeginning
        self.dayEnd=dayEnd
        self.breakfastTime=breakfastTime
        self.lunchTime=lunchTime
        self.dinnerTime=dinnerTime
        self.type=type