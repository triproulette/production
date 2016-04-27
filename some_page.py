import falcon


class Resource(object):

    def on_get(self, req, resp):
        resp.body = '{"message": "Tomer"}'
        resp.status = falcon.HTTP_200
