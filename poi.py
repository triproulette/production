import falcon
import json
import datetime
from APIHandler.poi_geosearch_api import POIGeosearch


class Resource(object):

    def on_get(self, req, resp, action, city):

        if action == 'get':
            if city == 'amsterdam':
                print 'amsterdam'
                poi_generator = POIGeosearch()
                results = poi_generator.call_api(latitude=52.310558, longitude=4.768221, radius=50)
                resp.body = results
                resp.status = falcon.HTTP_200
