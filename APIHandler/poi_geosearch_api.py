from abs_api_handler import APIHandler


class POIGeosearch(APIHandler):

    def __init__(self):
        self.apikey = "qvXIKasoUoG7AysZpsjURU01XSlsu2kb"
        APIHandler.__init__(self, "https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-circle/?")

    def call_api(self, latitude, longitude, radius):
        params = {"apikey": self.apikey, "latitude": latitude, "longitude": longitude, "radius": radius}
        APIHandler.serialize_params(self, params)
        return APIHandler.call_api(self)
