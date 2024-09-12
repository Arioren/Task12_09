from model import Target, Pilot, Aircraft


class Final_mission:

    def __init__(self, target:Target, aircraft:Aircraft , pilot:Pilot):
        self.city_name:str = target.city
        self.priority:int = target.priority
        self.assigend_pilot:str = pilot.name
        self.assigend_aircraft:str = aircraft.type
        self.distance:float = target.distance
        self.weather:dict = target.weather
        self.pilot_skill:int = pilot.skill
        self.aircraft_speed:int = aircraft.speed
        self.assigend_fuel_capacity:int = aircraft.fule_capacity
        self.fit_score:float = score(target, pilot, aircraft)


    def __repr__(self):
        return f"city: {self.city_name}, priority: {self.priority}, distance: {self.distance}, weather: {self.weather}"


def score(target, pilot, aircraft):
    return float((target.distance * 0.2) +
            (aircraft.fule_capacity * 0.25) +
            (pilot.skill * 0.25) +
            (wearher_score(target.weather["condintion"]) * 0.2) +
            (aircraft.speed * 0.1))

def wearher_score(weather):
    if(weather == 'Clear'):
        return 1.0
    elif(weather == 'Clouds'):
        return 0.7
    elif(weather == 'Rain'):
        return 0.5
    elif(weather == 'Stromy'):
        return 0.2
    else:
        return 0.0
