import csv
import json
import os
from uuid import uuid4
from utils import get_slow_cars,get_fast_cars,get_sport_cars,get_cheap_cars,get_medium_cars,get_expensive_cars, get_BMW_cars, get_Toyota_cars, get_Dacia_cars, get_Mercedes_cars, get_Golf_cars, get_Renault_cars, get_Ford_cars, get_Chevrolet_cars

if __name__ == '__main__':
    with open('cars.csv') as csv_file:
        data = []
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader):
            if index == 0:
                header = row
            else:
                data.append(row)

    my_cars = [
        {key: value for key, value in zip(header, row)}
        for row in data
    ]
    dict_cars_list = []
    for car in my_cars:
        my_cars = dict(car)
        my_cars["unique_id"] = str(uuid4())
        dict_cars_list.append(my_cars)
    print(get_slow_cars(dict_cars_list))

if 'output_data' not in os.listdir():
        os.mkdir('output_data')

with open('output_data/slow_cars.json', 'w') as json_file:
    json.dump(get_slow_cars(dict_cars_list), json_file, indent=2)

with open('output_data/fast_cars.json', 'w') as json_file:
    json.dump(get_fast_cars(dict_cars_list), json_file, indent=2)

with open('output_data/sport_cars.json', 'w') as json_file:
    json.dump(get_sport_cars(dict_cars_list), json_file, indent=2)

with open('output_data/cheap_cars.json', 'w') as json_file:
    json.dump(get_cheap_cars(dict_cars_list), json_file, indent=2)

with open('output_data/medium_cars.json', 'w') as json_file:
    json.dump(get_medium_cars(dict_cars_list), json_file, indent=2)

with open('output_data/expensive_cars.json', 'w') as json_file:
    json.dump(get_expensive_cars(dict_cars_list), json_file, indent=2)

with open('output_data/BMW_cars.json', 'w') as json_file:
    json.dump(get_BMW_cars(dict_cars_list), json_file, indent=2)

with open('output_data/Toyota_cars.json', 'w') as json_file:
    json.dump(get_Toyota_cars(dict_cars_list), json_file, indent=2)

with open('output_data/get_Dacia_cars.json', 'w') as json_file:
    json.dump(get_Dacia_cars(dict_cars_list), json_file, indent=2)

with open('output_data/Mercedes_cars.json', 'w') as json_file:
    json.dump(get_Mercedes_cars(dict_cars_list), json_file, indent=2)

with open('output_data/Golf_cars.json', 'w') as json_file:
    json.dump(get_Golf_cars(dict_cars_list), json_file, indent=2)

with open('output_data/Renault_cars.json', 'w') as json_file:
    json.dump(get_Renault_cars(dict_cars_list), json_file, indent=2)

with open('output_data/Ford_cars.json', 'w') as json_file:
    json.dump(get_Ford_cars(dict_cars_list), json_file, indent=2)

with open('output_data/Chevrolet_cars.json', 'w') as json_file:
    json.dump(get_Chevrolet_cars(dict_cars_list), json_file, indent=2)
