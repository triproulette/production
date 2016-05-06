import urllib
import urllib2
import json


class APIHandler(object):

    def __init__(self, resource):
        self.resource = resource
        self._url = None

    def serialize_params(self, params):
        self._url = self.resource + urllib.urlencode(params)

    def call_api(self):
        req = urllib2.Request(self._url)
        response = urllib2.urlopen(req)
        json_response = json.load(response)
        return json_response

