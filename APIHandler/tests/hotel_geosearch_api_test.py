from APIHandler.hotel_geosearch_api import HotelGeosearch


test = HotelGeosearch()
results = test.call_api(latitude=34.1504, longitude=-114.57632, radius=42,
                        check_in_date="2016-06-14", check_out_date="2016-06-16")
print results
