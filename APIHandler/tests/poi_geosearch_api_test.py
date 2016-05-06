from APIHandler.poi_geosearch_api import POIGeosearch
from Entities.POI import POI
from Entities.GeoLocation import GeoLocation


test = POIGeosearch()
results = test.call_api(latitude=52.374320, longitude=4.822390, radius=100)
pois = []

for poi in results["points_of_interest"]:
    pois.append(POI(poiID=0,title=poi["title"], description=poi["details"]["short_description"],
                    category="",
                    geoLocation=GeoLocation(latitude=poi["location"]["latitude"],
                                            longitude=poi["location"]["longitude"]),
                    grade=poi["grades"]['yapq_grade'],
                    activityTime=3,
                    image=poi["main_image"])
                )

for p in pois:
    try:
        print(p)
    except:
        continue
