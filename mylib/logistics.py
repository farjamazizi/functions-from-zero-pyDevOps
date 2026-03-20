"""
This module deals with logistics and calculates distanse between two points
and the time it takes to travel between two points and other logistics realted 
questions for a given speed.
"""
from geopy.distance import distance


USA_CITIES_COORDINATES = [
    {
        "city": "New York",
        "state": "New York",
        "latitude": 40.7128,
        "longitude": -74.0060,
    },
    {
        "city": "Los Angeles",
        "state": "California",
        "latitude": 34.0522,
        "longitude": -118.2437,
    },
    {
        "city": "Chicago",
        "state": "Illinois",
        "latitude": 41.8781,
        "longitude": -87.6298,
    },
    {"city": "Houston", "state": "Texas", "latitude": 29.7604, "longitude": -95.3698},
    {
        "city": "Phoenix",
        "state": "Arizona",
        "latitude": 33.4484,
        "longitude": -112.0740,
    },
    {
        "city": "Philadelphia",
        "state": "Pennsylvania",
        "latitude": 39.9526,
        "longitude": -75.1652,
    },
    {
        "city": "San Antonio",
        "state": "Texas",
        "latitude": 29.4241,
        "longitude": -98.4936,
    },
    {
        "city": "San Diego",
        "state": "California",
        "latitude": 32.7157,
        "longitude": -117.1611,
    },
    {"city": "Dallas", "state": "Texas", "latitude": 32.7767, "longitude": -96.7970},
    {
        "city": "Seattle",
        "state": "Washington",
        "latitude": 47.6062,
        "longitude": -122.3321,
    },
]


def _get_city_coordinates(city_name):
    for city in USA_CITIES_COORDINATES:
        if city["city"].lower() == city_name.lower():
            return (city["latitude"], city["longitude"])
    raise ValueError(f"City not found: {city_name}")


def find_coordinate(city_name):
    return _get_city_coordinates(city_name)


def distanse(city1, city2):
    coords1 = _get_city_coordinates(city1)
    coords2 = _get_city_coordinates(city2)
    return distance(coords1, coords2).miles


def total_distanse(cities):
    if len(cities) < 2:
        return 0

    total = 0
    for index in range(len(cities) - 1):
        total += distanse(cities[index], cities[index + 1])
    return total


# print(find_coordinate("Chicago"))
# print(distanse("New York", "Chicago"))
# print(total_distanse(["New York", "Chicago", "Seattle"]))
