import requests
from amadeus import Client, ResponseError
from travelengine.attractions.geocoding import get_lat_lon

amadeus = Client(
    client_id='GoSZ8yaI32CKz3zPPEYbCXuYk0pGXDYM',
    client_secret='xahrteSDFmMzmbEv'
)

try:
    place = "Barcelona, Spain"
    lat, lon = get_lat_lon(place)
    response = amadeus.reference_data.locations.points_of_interest.get(latitude=lat, longitude= lon)
    print(response.data)
except ResponseError as error:
    print(error)