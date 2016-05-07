import falcon
import json
import datetime
from APIHandler.poi_geosearch_api import POIGeosearch


class Resource(object):

    def on_get(self, req, resp, action, city):

        if action == 'get':
            if city == 'amsterdam':
                print req.uri
                print req.url
                poi_generator = POIGeosearch()
                results = poi_generator.call_api(latitude=52.310558, longitude=4.768221, radius=50)
                resp.body = '{"poi":[{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Amsterdam_-_Rembrandtplein.jpg/400px-Amsterdam_-_Rembrandtplein.jpg","title":"Rembrandtplein"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Amsterdam_-_Rembrandtplein.jpg/400px-Amsterdam_-_Rembrandtplein.jpg","title":"Rembrandtplein"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Amsterdam_-_Rembrandtplein.jpg/400px-Amsterdam_-_Rembrandtplein.jpg","title":"Rembrandtplein"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Amsterdam_-_Rembrandtplein.jpg/400px-Amsterdam_-_Rembrandtplein.jpg","title":"Rembrandtplein"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/NationaalMonumentVanuitReuzenrad.JPG/400px-NationaalMonumentVanuitReuzenrad.JPG","title":"Dam Square"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Amsterdam_oude_kerk2.jpg/300px-Amsterdam_oude_kerk2.jpg","title":"Oude Kerk"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Amsterdam_-_Rijksmuseum.jpg/400px-Amsterdam_-_Rijksmuseum.jpg","title":"Museumplein"}]}'
                resp.status = falcon.HTTP_200
