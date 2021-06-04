import requests
from amadeus import Client, ResponseError
from travelengine.attractions.geocoding import get_lat_lon
import json


amadeus = Client(
    client_id='GoSZ8yaI32CKz3zPPEYbCXuYk0pGXDYM',
    client_secret='xahrteSDFmMzmbEv'
)

def get_attractions(place):
    # Get list of attractions in place
    # place = "Barcelona, Spain"
    lat, lon = get_lat_lon(place)
    response = amadeus.reference_data.locations.points_of_interest.get(latitude=lat, longitude= lon)
    list_of_attractions = []
    for item in response.data:
        list_of_attractions.append(item["name"])
    print(list_of_attractions)

    #find lat,long of each attraction in list
    attraction_lat_lon_list = []

    # this is a very slow function
    for attraction in list_of_attractions:
        lat, lon = get_lat_lon(attraction)
        attraction_lat_lon_list.append(
            {
                "attraction": attraction,
                "lat": lat,
                "lon": lon,
            }
        )
    print(attraction_lat_lon_list)


def get_attractions2(place):
    print(place)

    secret = "5ae2e3f221c38a28845f05b6bd41f6a13ecd85a16c241187654ec0af"
    server = "https://api.opentripmap.com/0.1/en"
    endpoint = "/places/radius"

    params = {}
    params["radius"]= 48000
    params["apikey"] = secret
    try:
        lat, lon = get_lat_lon(place)
        params["lat"] = lat
        params["lon"] = lon
    except ResponseError as error:
        print(error)


    params["kinds"] = "foods"
    params["limit"] = 5
    resp = requests.get(server+ endpoint, params = params)
    obj = json.loads(resp.content)
    print(obj)


if __name__ == '__main__':
    get_attractions2("Ann Arbor")
