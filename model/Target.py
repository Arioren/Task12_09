from api.wearher_api import get_weather_by_city, get_distance


class Target:
    def __init__(self, city, priority):
        self.city:str = city
        self.priority:int = priority
        self.distance:float = get_distance(city)
        self.weather:dict = get_weather_by_city(city)

    def __repr__(self):
        return f"city: {self.city}, priority: {self.priority}, distance: {self.distance}, weather: {self.weather}"