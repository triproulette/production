import falcon
import some_page
import image
import index


api = application = falcon.API()

api.add_route('/some_page', some_page.Resource())
api.add_route('/image', image.Resource())
api.add_route('/trip', index.Resource())
