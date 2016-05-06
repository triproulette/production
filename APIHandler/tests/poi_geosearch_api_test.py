from APIHandler.poi_geosearch_api import POIGeosearch
from Entities.POI import POI


test = POIGeosearch()
results = test.call_api(latitude=52.374320, longitude=4.822390, radius=100)
pois = []

for poi in results["points_of_interest"]:
    print poi["title"]
    exit()
    pois.append(POI(poiID=0,title=poi["title"], description=,category=,grade=poi["grades"]['yapq_grade']))
