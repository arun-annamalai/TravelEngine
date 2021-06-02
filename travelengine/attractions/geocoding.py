import googlemaps
from datetime import datetime

def get_lat_lon(place):

    gmaps = googlemaps.Client(key='AIzaSyAJAEMdJU-N1tRwbTpkQXnrYX3N8CHW5lQ')

    # Geocoding an address
    geocode_result = gmaps.geocode(place)[0]
    # print(geocode_result)

    lat = geocode_result['geometry']['location']['lat']
    lon = geocode_result['geometry']['location']['lng']

    return lat, lon
    # Look up an address with reverse geocoding
    # everse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    # now = datetime.now()
    # directions_result = gmaps.directions("Sydney Town Hall",
    #                                      "Parramatta, NSW",
    #                                      mode="transit",
    #                                      departure_time=now)
