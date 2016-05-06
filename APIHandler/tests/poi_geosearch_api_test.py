from APIHandler.poi_geosearch_api import POIGeosearch


test = POIGeosearch()
results = test.call_api(latitude=35.1504, longitude=-114.57632, radius=42)
print results
