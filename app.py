import falcon
import trip
import user
import trip_generator


api = application = falcon.API()

#api.add_route('/some_page', some_page.Resource())
#api.add_route('/image', image.Resource())

api.add_route('/trip_generate/{action}/{user_id}', trip_generator.Resource())
api.add_route('/trip/{trip_id}/{action}/{event_id}', trip.Resource())
api.add_route('/user/{action}/{id}/{fullname}/{avatar}', user.Resource())
