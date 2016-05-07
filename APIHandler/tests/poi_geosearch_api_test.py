from APIHandler.poi_geosearch_api import POIGeosearch
import json


test = POIGeosearch()
results = test.call_api(latitude=52.310558, longitude=4.768221, radius=100)

print results
