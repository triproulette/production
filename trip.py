import falcon
import json
from DBHandler import DBHandler
from DBHandler import DBConnection
from algo.trip_roulette import TripRoulette
import datetime


class Resource(object):

    def on_get(self, req, resp, trip_id, action, event_id):

        if action == 'get_event':
            ev_count = 5    # 4 events each request

            conn = DBConnection.DBConnection()
            handler = DBHandler.DBHandler(conn)
            #   get next ev_count events
            results = handler.query("SELECT e.id,p.title,p.description,p.category,e.s_time, e.e_time "+
                                    "FROM tr_db.poi as p JOIN tr_db.event as e ON e.poi_id = p.id "+
                                    "ORDER BY e.id ASC LIMIT {},{}".format(event_id,ev_count))

            json_event = ()
            for i in range(ev_count):
                try:
                    ev = '{{ {} }}'.format(dict(results[i]))
                    print ev
                    json_event.append(ev)
                except:
                    print 'error appending'
                    continue

            resp.body = '{{ events: [ {} ] }}'.format(', '.join(json_event))
            resp.status = falcon.HTTP_200

    def on_get(self, req, resp, action, user_id):

        if action == 'generate':

            generator = TripRoulette(0, "paris", datetime(2016,05,07,8,0,0), datetime(2016,05,12,21,0,0))
            generator.generate_random_trip()

            resp.body = ''
            resp.status = falcon.HTTP_200
