import falcon


class Resource(object):

    def on_get(self, req, resp):
        resp.body = '{"message": "!afafa!@kod! up!dated!!!!!!"}'
        resp.status = falcon.HTTP_200
#sandak
#Tomer
#bar