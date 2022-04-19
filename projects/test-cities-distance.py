import unittest
from math import radians, cos, sin, asin, sqrt
from urllib.request import urlopen
import ssl

URL = "https://devw.github.io/supn/data/laposte_hexasmal.small.csv"


def get_city_GCS(url=URL):
    # TODO
    # Write a function called get_city_GCS.
    # INPUT
    # The function must have one parameter, the URL that points to the cities' dataset.
    # As an example consider the dataset available at this address "https://devw.github.io/supn/data/laposte_hexasmal.small.csv"
    # OUTPUT
    # The function must return a dictionary
    # The dictionary's keys represent the cities' names and the value of each key the latitude and longitude of the city given as a key
    # Example:
    # {'London': '51.509865,-0.118092', 'Paris': '48.864716,2.349014'}
    response = urlopen(url, context=ssl._create_unverified_context())
    raw_data = response.read().decode('utf-8')
    lines = [line.split(";") for line in raw_data.split("\r\n")][1:-1]
    return {line[1]: line[5] for line in lines}


def get_distance(lonLat_1, lonLat_2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    lon1, lat1 = lonLat_1.split(",")
    lon2, lat2 = lonLat_2.split(",")
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(
        radians, [float(lon1), float(lat1), float(lon2), float(lat2)])

    # haversine formula
    dlon, dlat = lon2 - lon1, lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    r = 6371
    return c * r


def get_distances_from(city):
    # TODO
    # Write a function called get_distances_from.
    # INPUT
    # The function must accept as input one parameter, the city name (e.g. ALLAN).
    # OUTPUT
    # The function returns as output a dictionary
    # the dictionary has as keys the cities' names and as their value, the distances in km from the city specified as a parameter
    # Example
    # If ALLAN is the input, the output should be this
    # {'ALLAN': 0.0, 'CHATEAUNEUF DU RHONE': 8.29215195136882, 'CHAMARET': 14.009638918175074, ... }
    city_dict = get_city_GCS()
    city_distances = dict()
    lonLat_1 = city_dict[city]
    for city in city_dict:
        lonLat_2 = city_dict[city]
        city_distances[city] = get_distance(lonLat_1, lonLat_2)
    return city_distances


def get_sorted_distance(distances):
    # TODO
    # Write a function named get_sorted_distance
    # INPUT
    # The function must accept as input a dictionary where the keys represents the cities' names and the values represents the distance in km
    # OUTPUT
    # The function returns as output the same dictionary having the key sorted based on the values.
    # Example
    # INPUT -> {'Rome': 100, 'Paris': 12, 'London': 40 }
    # OUTPUT -> {'Paris': 12, 'London': 40, 'Rome': 100}
    return {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}


class Logger:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def debug(msg):
        start_end = "\n**************************************************** **:\n"
        return f"{Logger.OKGREEN} {start_end} {msg} {start_end} {Logger.ENDC}"

    @staticmethod
    def error(msg):
        start_end = "\n**************************************************** **:\n"
        return f"{Logger.FAIL} {start_end} {msg} {start_end} {Logger.ENDC}"


class TestGraphicalInterface(unittest.TestCase):
    ### Testing ### 
    def test_get_city_GCS(self):
        print(Logger.debug("Testing get_city_GCS function"))
        url = "https://devw.github.io/supn/data/laposte_hexasmal.small.csv"
        city_dict = get_city_GCS(url)
        print(city_dict)
        assert type(city_dict) == dict
        assert len(city_dict) == 28
        assert city_dict['CLAVEYSON'] == '45.173018025,4.933788902'

    def test_get_distances_from(self):
        city = 'ALLAN'
        distances_from = get_distances_from(city)
        print(Logger.debug("Testing get_distances_from function"))
        print(f"\n**Distances_from {city}:\n {distances_from} ")
        assert type(distances_from) == dict
        assert distances_from['ARNAYON'] < distances_from['AULAN']

    def test_get_sorted_distance(self):
        print(Logger.debug("Testing get_sorted_distance function"))
        city = "ALLAN"
        distances_from = get_distances_from(city)
        sorted_distance = get_sorted_distance(distances_from)
        print(f"\nsorted_distance: \n {sorted_distance}")
        city_list = list(sorted_distance)
        assert type(sorted_distance) == dict
        assert sorted_distance[city_list[1]] < sorted_distance[city_list[2]]
        assert sorted_distance[city_list[-2]] < sorted_distance[city_list[-1]]


if __name__ == '__main__':
    unittest.main()
