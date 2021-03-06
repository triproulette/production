import falcon
import json
import datetime
import re
from APIHandler.poi_geosearch_api import POIGeosearch


class Resource(object):

    def on_get(self, req, resp, action, city):

        if action == 'get':
            if city == 'amsterdam':
                try:
                    print req.query_string
                    #print req.path
                    g = re.search(r'jQuery[^\&]*',req.query_string)
                    g = g.group(0)
                    poi_generator = POIGeosearch()
                    results = poi_generator.call_api(latitude=52.310558, longitude=4.768221, radius=50)
                    resp.body = g + '({"poi":[{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/MelkwegAmsterdam.jpg/400px-MelkwegAmsterdam.jpg","title":"Melkweg"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Leidseplein.jpg/400px-Leidseplein.jpg","title":"Leidseplein"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Amsterdam_rijkmuseum.JPG/400px-Amsterdam_rijkmuseum.JPG","title":"Rijksmuseum"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Amsterdam_-_Rembrandtplein.jpg/400px-Amsterdam_-_Rembrandtplein.jpg","title":"Rembrandtplein"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/NationaalMonumentVanuitReuzenrad.JPG/400px-NationaalMonumentVanuitReuzenrad.JPG","title":"Dam Square"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Amsterdam_oude_kerk2.jpg/300px-Amsterdam_oude_kerk2.jpg","title":"Oude Kerk"},{"main_image":"https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Amsterdam_-_Rijksmuseum.jpg/400px-Amsterdam_-_Rijksmuseum.jpg","title":"Museumplein"}]})'
                    resp.status = falcon.HTTP_200
                except:
                    pass
