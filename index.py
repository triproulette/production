import falcon


class Resource(object):

    def on_get(self, req, resp):
        resp.body = ''
        resp.status = falcon.HTTP_200
#sandak
#Tomer
#bar
#asaf