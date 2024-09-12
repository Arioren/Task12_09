import math
from functools import partial

import requests
from toolz import pipe
from toolz.curried import get_in



def get_weater(url):
    response = requests.request("GET", url)
    return response.json()

def get_distance(city):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid=903391243cc8487527d150ca6cb0c427"
    try:
        response = requests.request("GET", url)
        lat = response.json()[0]['lat']
        lon = response.json()[0]['lon']
        return haversine_distance(lat, lon, 32.06694,34.77778)
    except Exception as e:
        print(e)
        return None

def get_weather_by_city(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=903391243cc8487527d150ca6cb0c427"
    try:
        response = requests.request("GET", url)
        return pipe(
            response.json(),
            lambda x: x['list'],
            partial(filter, lambda x: x['dt_txt'] == '2024-09-13 00:00:00'),
            list,
            lambda x: {'condintion': x[0]['weather'][0]["main"], 'clouds': x[0]['clouds']["all"], "wind": x[0]['wind']["speed"]}
        )
    except Exception as e:
        print(e)
        return []


# Function to calculate the distance between two coordinates using the Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0 # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon /
    2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance