from APIHandler.poi_geosearch_api import POIGeosearch
from Entities.POI import POI
from Entities.GeoLocation import GeoLocation


test = POIGeosearch()
results = test.call_api(latitude=52.374320, longitude=4.822390, radius=100)

for poi in results:
    print poi