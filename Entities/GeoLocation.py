class GeoLocation(object):

    def __init__(self, longitude, latitude):
        self._latitude = latitude
        self._longitude = longitude

    def __str__(self):
        return str(self._latitude).encode('utf-8') + ","+ str(self._longitude).encode('utf-8')