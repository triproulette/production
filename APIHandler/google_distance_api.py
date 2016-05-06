from abs_api_handler import APIHandler


class GoogleDistance(APIHandler):

    def __init__(self):
        self.apikey = "AIzaSyA9UwHPOJ3JLbnrK8P3wgcSWLXgCXOCkFo"
        APIHandler.__init__(self, "https://maps.googleapis.com/maps/api/distancematrix/json?")

    def call_api(self, o_latitude, o_longitude, d_latitude, d_longitude):
        params = {"apikey": self.apikey, "origins": str(o_latitude) + "," + str(o_longitude),
                  "destinations": str(d_latitude) + "," + str(d_longitude)}
        APIHandler.serialize_params(self, params)
        raw_json = APIHandler.call_api(self)
        return raw_json["rows"][0]["elements"][0]["duration"]["value"] # seconds
