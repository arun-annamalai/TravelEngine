from travelengine.attractions.attractions import get_attractions
from travelengine.attractions.attractions import attraction

import sklearn

from travelengine.kmeans.kmeans import get_features, get_weights
try:
    print("Welcome to our Hotel Finder. Which City would you like to visit? Format: City, Country")
    location = input()
    print("The different categories to consider are: foods, shops, museums, historic_architecture, theatres_and_entertainments, nightclubs.")
    print("Please enter in comma-seperated form a rating of 1-10 for each category respectively.")
    ratings = input()
    ratings_list = ratings.split(',')
    ratings_list = [int(x) for x in ratings_list]
    assert(len(ratings_list) == 6)
    weightings = {
        "foods": ratings_list[0],
        "shops": ratings_list[1],
        "museums": ratings_list[2],
        "historic_architecture": ratings_list[3],
        "theatres_and_entertainments": ratings_list[4],
        "nightclubs": ratings_list[5],

    }

    total_attractions = []
    for cat, weight in weightings:
        total_attractions.append(get_attractions(location, cat))

    coordinates = get_features(total_attractions)
    weights = get_weights(total_attractions, weightings)





except ResponseError as error:
    print(error)