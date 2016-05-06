from APIHandler.hotel_geosearch_api import HotelGeosearch


test = HotelGeosearch()
results = test.call_api(latitude=32.096306, longitude=34.783167, radius=100,
                        check_in_date="2016-06-14", check_out_date="2016-06-16")

for p in results:
    print(p)