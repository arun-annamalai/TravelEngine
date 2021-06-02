import requests
from amadeus import Client, ResponseError
from travelengine.attractions.geocoding import get_lat_lon

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

