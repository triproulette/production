from APIHandler.abs_api_handler import APIHandler
from Entities.POI import POI
from Entities.GeoLocation import GeoLocation


class POIGeosearch(APIHandler):

    def __init__(self):
        self.apikey = "qvXIKasoUoG7AysZpsjURU01XSlsu2kb"
        APIHandler.__init__(self, "https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-circle/?")

    def call_api(self, latitude, longitude, radius):
        params = {"apikey": self.apikey, "latitude": latitude, "longitude": longitude, "radius": radius}
        APIHandler.serialize_params(self, params)
        raw_json = APIHandler.call_api(self)
        pois = []

        """
        for poi in raw_json["points_of_interest"]:
            pois.append(POI(title=poi["title"], description=poi["details"]["short_description"],
                            category="",
                            geoLocation=GeoLocation(latitude=poi["location"]["latitude"],
                                                    longitude=poi["location"]["longitude"]),
                            grade=poi["grades"]['yapq_grade'],
                            activityTime=3,
                            image=poi["main_image"])
                        )
        return pois
        """
        return raw_json["points_of_interest"]