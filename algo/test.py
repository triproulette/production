from trip_roulette import TripRoulette
import datetime

generator = TripRoulette(0, "paris", datetime(2016,05,07,8,0,0), datetime(2016,05,12,21,0,0))
generator.generate_random_trip()
