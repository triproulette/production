from abs_api_handler import APIHandler


class HotelGeosearch(APIHandler):

    def __init__(self):
        self.apikey = "qvXIKasoUoG7AysZpsjURU01XSlsu2kb"
        APIHandler.__init__(self, "https://api.sandbox.amadeus.com/v1.2/hotels/search-circle/?")

    def call_api(self, latitude, longitude, radius, check_in_date, check_out_date):
        params = {"apikey": self.apikey, "latitude": latitude, "longitude": longitude, "radius": radius,
                  "check_in": check_in_date, "check_out": check_out_date}
        APIHandler.serialize_params(self, params)
        return APIHandler.call_api(self)
