from symbol import lambdef_nocond

from toolz import pipe
from toolz.curried import partial, reduce

from api.wearher_api import get_weater
from model.Final_mission import Final_mission
from model.Target import Target
from repository.csv_repository import write_person_to_csv
from repository.json_repository import write_to_file, read_json, convert_from_json_to_target
from services import create_array_target, create_array_pilot, create_array_aircraft, find_best_matches_for_one_target

#my api addresses
API_URL_DATA =\
    lambda x: f'https://api.openweathermap.org/data/2.5/forecast?q={x}&appid=903391243cc8487527d150ca6cb0c427'
API_URL_LOCATION =\
    lambda x: f'https://api.openweathermap.org/geo/1.0/direct?q={x}&appid=903391243cc8487527d150ca6cb0c427'


#מראה שימוש בקריאה וכתיבה לקובץ
#call api
weater_get_api = get_weater(API_URL_DATA("Damascus"))
#write to file
write_to_file("repository/Damascus.json")(weater_get_api)

#read from file
tmp = read_json()("repository/Damascus.json")
#find the relevant date and time
print(pipe(
    tmp,
    lambda x: x['list'],
    partial(filter, lambda x: x['dt_txt'] == '2024-09-13 00:00:00'),
    list
))

#STATR MY PROJECT

#read the all cities
my_json_targets = read_json("repository/cities.json")

#read the pilot
json_pilot = read_json("repository/piolt.json")

#read the aircraft
json_aircraft = read_json("repository/aircraft.json")

#my array of targets with distance and weather
targets_array = create_array_target()(my_json_targets)

#my array of pilots
pilot_array = create_array_pilot()(json_pilot)

#my array of aircraft
aircraft_array = create_array_aircraft()(json_aircraft)

#מראה שהקריאות עבדו כצריך

print(targets_array)
print(pilot_array)
print(aircraft_array)

#ניסיון שלא צלח בתכנון פונקציונלי
#know we find best matches for each target
# print(pipe(
#     targets_array,
#     partial(sorted, key=lambda x: x.priority, reverse=True),
#     lambda x: x[:7],
#     partial(map, lambda x:find_best_matches_for_one_target(x, pilot_array, aircraft_array) ),
#     partial(sorted, key=lambda x: x.fit_score, reverse=True),
#     list
# ))

result = []
for aircraft in aircraft_array:
    for pilot in pilot_array:
        for target in targets_array:
            result.append(Final_mission(target, aircraft, pilot))

result.sort(key=lambda x: x.fit_score, reverse=True)

final_result = []

index = 0
while result:
    final_result.append(result[0])
    result = list(filter(lambda x: x.city_name != final_result[index].city_name and x.assigend_pilot != final_result[index].assigend_pilot and x.assigend_aircraft != final_result[index].assigend_aircraft, result))
    index += 1

write_person_to_csv(final_result, "repository/result.csv")




