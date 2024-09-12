import json

from toolz import curry

from model.Aircraft import Aircraft
from model.Pilot import Pilot
from model.Target import Target


# Reads data from a JSON file
@curry
def read_json(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(e)
        return []

# Writes data to a JSON file
@curry
def write_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def convert_from_json_to_target(json):
    return Target(
        json['city'],
        json['priority']
    )

def convert_from_json_to_pilot(json):
    return Pilot(
        json['name'],
        json['skill']
    )

def convert_from_json_to_aircraft(json):
    return Aircraft(
        json['type'],
        json['speed'],
        json['fule_capacity']
    )