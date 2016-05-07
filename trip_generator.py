import falcon
import json
from DBHandler import DBHandler
from DBHandler import DBConnection
from algo.trip_roulette import TripRoulette
import datetime


class Resource(object):

    def on_get(self, req, resp, action, user_id):

        if action == 'generate':

            generator = TripRoulette(0, "paris", datetime(2016,05,07,8,0,0), datetime(2016,05,12,21,0,0))
            generator.generate_random_trip()

            resp.body = ''
            resp.status = falcon.HTTP_200
