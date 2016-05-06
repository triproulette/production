from APIHandler.google_distance_api import GoogleDistance
from APIHandler.hotel_geosearch_api import HotelGeosearch
from DBHandler import DBHandler
from Entities import POI
from Entities import Event

import datetime

def stepGenerator(prop,prevnt):
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
        foodPoi._activityTime = datetime.timedelta(hours=1, minutes=30)

        food_ev = Event.Event()
        food_ev._poiID=foodPoi.save_to_db()
        food_ev._startTime=prev_poi._activityTime
        food_ev._endTime=prev_poi._activityTime+ datetime.timedelta(hours=1, minutes=30)
        return food_ev.save_to_db()


    if abs(prevnt.endTime - prop._lunchTime) < datetime.timedelta(days=0, hours=1, minutes=0, seconds=0, microseconds=0):
        foodPoi = POI.POI()
        foodPoi._title = "lunch"
        foodPoi._description = "lunch time"
        foodPoi._category = "food"
        foodPoi._geoLocation = prev_poi._geoLocation
        foodPoi._grade = 0
        foodPoi._activityTime = datetime.timedelta(hours=1, minutes=30)

        food_ev = Event.Event()
        food_ev._poiID = foodPoi.save_to_db()
        food_ev._startTime = prev_poi._activityTime
        food_ev._endTime = prev_poi._activityTime + datetime.timedelta(hours=1, minutes=30)
        return food_ev.save_to_db()

    if abs(prevnt.endTime - prop._dinnerTime) < datetime.timedelta(days=0, hours=1, minutes=0, seconds=0, microseconds=0):
        foodPoi = POI.POI()
        foodPoi._title = "dinner"
        foodPoi._description = "dinner time"
        foodPoi._category = "food"
        foodPoi._geoLocation = prev_poi._geoLocation
        foodPoi._grade = 0
        foodPoi._activityTime = datetime.timedelta(hours=1, minutes=30)

        food_ev = Event.Event()
        food_ev._poiID = foodPoi.save_to_db()
        food_ev._startTime = prev_poi._activityTime
        food_ev._endTime = prev_poi._activityTime + datetime.timedelta(hours=1, minutes=30)
        return food_ev.save_to_db()


    if abs(prevnt.endTime - prop._dayEnd) < datetime.timedelta(days=0, hours=1, minutes=0, seconds=0, microseconds=0):
       api = HotelGeosearch()
       results = api.call_api(prev_poi._geoLocation._latitude , prev_poi._geoLocation._longitude, radius=100, check_in_date=prevnt._endtime.isoformat(), check_out_date= prevnt._endtime + datetime.datetime.timedelta(days=1).replace(prop._dayBeginning)).save_to_db()


    def algo_grade_calc():