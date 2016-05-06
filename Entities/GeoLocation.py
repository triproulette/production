class GeoLocation(object):

    def __init__(self, longitude, latitude):
        self._latitude = latitude
        self._longitude = longitude

    def get_location(self):
        return str(self._latitude) + ","+ str(self._longitude)