import falcon


class Resource(object):

    def on_get(self, req, resp):
        resp.body = '{"message": "code updated!!!"}'
        resp.status = falcon.HTTP_200
#sandak
#Tomer
#bar
#asaf