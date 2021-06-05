import requests
from amadeus import Client, ResponseError
from travelengine.attractions.geocoding import get_lat_lon
import json

amadeus = Client(
    client_id='GoSZ8yaI32CKz3zPPEYbCXuYk0pGXDYM',
    client_secret='xahrteSDFmMzmbEv'
)


class attraction:
    def __init__(self, name, lat, lon, category):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.category = category

    def __str__(self):
        return f'Name: {self.name} lat: {self.lat} lon: {self.lon} category: {self.category}'


def get_attractions(place, category):
    secret = "5ae2e3f221c38a28845f05b6bd41f6a13ecd85a16c241187654ec0af"
    server = "https://api.opentripmap.com/0.1/en"
    endpoint = "/places/radius"

    params = {}
    params["radius"] = 48000
    params["apikey"] = secret
    try:
        lat, lon = get_lat_lon(place)
        params["lat"] = lat
        params["lon"] = lon
    except ResponseError as error:
        print(error)

    params["kinds"] = category
    params["limit"] = 5
    resp = requests.get(server + endpoint, params=params)
    response = json.loads(resp.content)

    attractions_list = []
    for attr_json in response['features']:
        name = attr_json['properties']['name']
        lat = attr_json['geometry']['coordinates'][1]
        lon = attr_json['geometry']['coordinates'][0]
        category = category
        new_attraction = attraction(name, lat, lon, category)
        attractions_list.append(new_attraction)
    return attractions_list


def get_nearest_hotel(lat, lon):
    secret = "5ae2e3f221c38a28845f05b6bd41f6a13ecd85a16c241187654ec0af"
    server = "https://api.opentripmap.com/0.1/en"
    endpoint = "/places/radius"
    params = {}
    params["lat"] = lat
    params["lon"] = lon
    params["radius"] = 10000
    params["kinds"] = "other_hotels"
    params["limit"] = 3
    params["apikey"] = secret
    resp = requests.get(server + endpoint, params=params)
    response = json.loads(resp.content)
    print("Here are the best hotels to stay at based on what you value most!")
    for feature in response["features"]:
        print(feature["properties"]["name"])


if __name__ == '__main__':
    get_nearest_hotel(42.2808, -83.7430)
    # get_attractions("Ann Arbor", "foods")
