import csv
from model import Final_mission


def write_person_to_csv(final_missions:list[Final_mission] , filepath: str):
    try:
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=['Target City', 'Priority', 'Assigned Pilot', 'Assigned Aircraft', 'Distance', 'Weather', 'Pilot Skill', 'Aircraft Speed', 'Assigned Fuel Capacity', 'Fit Score'])
            csv_writer.writeheader()
            for final_mission in final_missions:
                csv_writer.writerow({
                    'Target City': final_mission.city_name,
                    'Priority': final_mission.priority,
                    'Assigned Pilot': final_mission.assigend_pilot,
                    'Assigned Aircraft': final_mission.assigend_aircraft,
                    'Distance': final_mission.distance,
                    'Weather': final_mission.weather,
                    'Pilot Skill': final_mission.pilot_skill,
                    'Aircraft Speed': final_mission.aircraft_speed,
                    'Assigned Fuel Capacity': final_mission.assigend_fuel_capacity,
                    'Fit Score': final_mission.fit_score
                })
    except Exception as e:
        print(e)