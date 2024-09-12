import math
from functools import partial, reduce
from toolz import compose, pipe, first

from model.Final_mission import Final_mission
from repository.json_repository import convert_from_json_to_target, convert_from_json_to_pilot, \
    convert_from_json_to_aircraft


def create_array_target():
    return compose(
        list,
        partial(map, convert_from_json_to_target)
    )

def create_array_pilot():
    return compose(
        list,
        partial(map, convert_from_json_to_pilot)
    )

def create_array_aircraft():
    return compose(
        list,
        partial(map, convert_from_json_to_aircraft)
    )

###################################################################################
#כאן ניסיתי לעשות את הנדרש בתכנון פונקציונלי אך לא הצלחתי
##################################################################################
def find_best_matches_for_one_target(target, pilot_array, aircraft_array):
    return pipe(
        pilot_array,
        lambda tmp:reduce( lambda x , y: x + find_best_matches_for_one_target_for_one_pilot(target, y, aircraft_array), tmp, list()),
        partial(sorted,key=lambda x: x.fit_score, reverse=True),
        first
    )

def find_best_matches_for_one_target_for_one_pilot(target, pilot, aircraft_array):
    return pipe(
        aircraft_array,
        partial(map, lambda x: Final_mission(target, x, pilot)),
        list
    )