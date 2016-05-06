from APIHandler.google_distance_api import GoogleDistance
from DBHandler import DBHandler
from Entities import POI
from Entities import Event

import datetime

def stepGenerator(prop,prevnt, curevnt,):
    db = DBHandler.DBHandler()
    ##normalization
    population_grade = curevnt/5;
    api = GoogleDistance()
    prev_poi = db.getPoi(prevnt.eventID)
    curr_poi = db.getPoi(curevnt.eventID)
    distance = api.call_api(prev_poi._geoLocation._latitude , prev_poi._geoLocation._longitude, curr_poi._geoLocation._latitude , curr_poi._geoLocation._longitude)
    if distance > 210:
        distance_grade = 0
    else:
        distance_grade = distance/210

    ##prop calc

    if abs(prevnt.endTime-prop.breakfastTime) < datetime.timedelta(days=0, hours=1, minutes=0, seconds=0, microseconds=0) :
        foodPoi = POI.POI()
        foodPoi._title = "breakfast"
        foodPoi._description = "breakfast time"
        foodPoi._category = "food"
        foodPoi._geoLocation = prev_poi._geoLocation
        foodPoi._grade = 0
        foodPoi._activityTime = prev_poi._activityTime

        food_ev = Event.Event()


