import falcon
import some_page
import image


api = application = falcon.API()

api.add_route('/index', some_page.Resource())
api.add_route('/image', image.Resource())
