from travelengine.attractions.attractions import get_attractions, get_nearest_hotel
from travelengine.attractions.attractions import attraction

from travelengine.kmeans.kmeans import get_features, get_weights, cluster_attractions
import traceback

try:
    print("Welcome to our Hotel Finder. Which City would you like to visit? Format: City, Country")
    location = input()
    print(
        "The different categories to consider are: foods, shops, museums, historic_architecture, theatres_and_entertainments, nightclubs.")
    print("Please enter in comma-seperated form a rating of 1-10 for each category respectively.")
    ratings = input()
    ratings_list = ratings.split(',')
    assert (len(ratings_list) == 6)
    ratings_list = [int(x) for x in ratings_list]
    weightings = {
        "foods": ratings_list[0],
        "shops": ratings_list[1],
        "museums": ratings_list[2],
        "historic_architecture": ratings_list[3],
        "theatres_and_entertainments": ratings_list[4],
        "nightclubs": ratings_list[5],

    }

    print(weightings)
    total_attractions = []
    for cat, weight in weightings.items():
        total_attractions.append(get_attractions(location, cat))

    coordinates = get_features(total_attractions)
    weights = get_weights(total_attractions, weightings)
    center = cluster_attractions(coordinates, weights)

    print("this is the center")
    print(center)

    # just have to figure out how to extract lat, lon from center and then call get_nearest_hotel function
    lat = center[0][0]
    lon = center[0][1]
    get_nearest_hotel(lat, lon)
except Exception:
    print(traceback.print_exc())
