from travelengine.attractions.attractions import get_attractions

try:
    print("Welcome to our Hotel Finder. Which City would you like to visit? Format: City, Country")
    location = input()
    print("Do you want to consider popular restaurants in your hotel search (Yes/No)?")
    restaurant_answer = input()
    restaurant_wanted_bool = False
    if restaurant_answer == "Yes":
        restaurant_wanted_bool = True
    get_attractions(location)
except ResponseError as error:
    print(error)