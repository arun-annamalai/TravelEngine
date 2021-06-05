import pandas
import sklearn
from sklearn.cluster import KMeans
from travelengine.attractions.attractions import attraction
from travelengine.attractions.attractions import get_attractions

# returns the x and y coordinates of each attractions
def get_features(attractions_list):
    ml_input = []
    for list in attractions_list:
        for attraction in list:
            print(attraction.lat)
            ml_input.append([attraction.lat, attraction.lon])
    return ml_input

def get_weights(attractions_list, weightings_dict):
    weights = []
    for list in attractions_list:
        for attraction in list:
            weights.append(weightings_dict[attraction.category])
    return weights


def cluster_attractions(coordinates, weights):
    # kmeans is an object created by sklean which holds properties and the ML algorithm
    kmeans = KMeans(n_clusters = 1, verbose = 1)

    cluster_indexes = kmeans.fit_predict(coordinates, sample_weight=weights)

    # cluster center is a list of centers of clusters (x,y coordinates)
    cluster_centers = kmeans.cluster_centers_
    # cluster_errors = kmeans._interia

    return cluster_centers



def get_location(coordinates_list):
    pass

if __name__ == '__main__':
    get_attractions("Ann Arbor", "foods")

