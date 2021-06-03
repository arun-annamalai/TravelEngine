import requests
from amadeus import Client, ResponseError
from travelengine.attractions.geocoding import get_lat_lon
import json


def get_attractions(place = "Barcelona, Spain"):
    amadeus = Client(
        client_id='GoSZ8yaI32CKz3zPPEYbCXuYk0pGXDYM',
        client_secret='xahrteSDFmMzmbEv'
    )

    try:
        lat, lon = get_lat_lon(place)
        response = amadeus.reference_data.locations.points_of_interest.get(latitude=lat, longitude= lon)
        print(response.data)
    except ResponseError as error:
        print(error)


def get_attractions2(place):
    print(place)

    secret = "5ae2e3f221c38a28845f05b6bd41f6a13ecd85a16c241187654ec0af"
    server = "https://api.opentripmap.com/0.1/en"
    endpoint = "/places/radius"

    params = {}
    params["radius"]= 1600
    params["apikey"] = secret
    try:
        lat, lon = get_lat_lon(place)
        params["lat"] = lat
        params["lon"] = lon
    except ResponseError as error:
        print(error)

    params['rate'] = 3

    resp = requests.get(server+ endpoint, params = params)
    obj = json.loads(resp.content)
    print(obj)


if __name__ == '__main__':
    get_attractions2("Ann Arbor")