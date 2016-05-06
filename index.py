import falcon


class Resource(object):

    def on_get(self, req, resp):

        resp.body = '{"msg": "bla"}'
        resp.status = falcon.HTTP_200