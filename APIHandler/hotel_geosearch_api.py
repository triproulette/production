from abs_api_handler import APIHandler
from Entities.POI import POI
from Entities.GeoLocation import GeoLocation


class HotelGeosearch(APIHandler):

    def __init__(self):
        self.apikey = "qvXIKasoUoG7AysZpsjURU01XSlsu2kb"
        APIHandler.__init__(self, "https://api.sandbox.amadeus.com/v1.2/hotels/search-circle/?")

    def call_api(self, latitude, longitude, radius, check_in_date, check_out_date):
        params = {"apikey": self.apikey, "latitude": latitude, "longitude": longitude, "radius": radius,
                  "check_in": check_in_date, "check_out": check_out_date}
        APIHandler.serialize_params(self, params)
        raw_json = APIHandler.call_api(self)
        pois = []
        for poi in raw_json["results"]:
            pois.append(POI(poiID=0,title=poi["property_name"],
                            activityTime=0,
                            category="Hotel",
                            description="",
                            geoLocation=GeoLocation(latitude=poi["location"]["latitude"]
                                                    ,longitude=poi["location"]["longitude"]),
                            grade=poi["min_daily_rate"]["amount"],
                            image=""))
        return pois
