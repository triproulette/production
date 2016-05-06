from APIHandler.abs_api_handler import APIHandler

test = APIHandler("https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-circle/?")
test.serialize_params({"apikey": "qvXIKasoUoG7AysZpsjURU01XSlsu2kb", "latitude": "35.1504", "longitude": "-114.57632",
                       "radius": "42"})
res = test.call_api()
print res

##k