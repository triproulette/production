import falcon
import some_page
import image
import index
import trip


api = application = falcon.API()

api.add_route('/some_page', some_page.Resource())
api.add_route('/image', image.Resource())
api.add_route('/trip', index.Resource())
api.add_route('/trip/{trip_id}/get_poi/{poi_id}', trip.Resource())
