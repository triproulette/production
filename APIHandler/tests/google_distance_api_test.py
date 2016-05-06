from APIHandler.google_distance_api import GoogleDistance


test = GoogleDistance()
results = test.call_api(o_latitude=32.185735, o_longitude=34.819983, d_latitude=32.236455,d_longitude=34.871290)
print results
