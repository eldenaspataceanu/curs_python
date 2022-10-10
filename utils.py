def get_slow_cars(dict_cars_list):

    slow_cars = [dic_car for dic_car in dict_cars_list if int(dic_car.get("hp")) < 120]
    return slow_cars

def get_fast_cars(dict_cars_list):

    fast_cars = [dic_car for dic_car in dict_cars_list if int(dic_car.get("hp")) >= 120 and int(dic_car.get("hp")) < 180]
    return fast_cars

def get_sport_cars(dict_cars_list):

    sport_cars = [dic_car for dic_car in dict_cars_list if int(dic_car.get("hp")) >= 180]
    return sport_cars

def get_cheap_cars(dict_cars_list):

    cheap_cars = [dic_car for dic_car in dict_cars_list if int(dic_car.get("price")) < 1000]
    return cheap_cars

def get_medium_cars(dict_cars_list):

    medium_cars = [dic_car for dic_car in dict_cars_list if int(dic_car.get("price")) >= 1000 and int(dic_car.get("price")) < 5000 ]
    return medium_cars

def get_expensive_cars(dict_cars_list):

    expensive_cars = [dic_car for dic_car in dict_cars_list if int(dic_car.get("price")) >= 5000]
    return expensive_cars

def get_BMW_cars(dict_cars_list):

    BMW_cars = [dic_car for dic_car in dict_cars_list if dic_car.get("brand") == 'BMW']
    return BMW_cars

def get_Toyota_cars(dict_cars_list):

    Toyota_cars = [dic_car for dic_car in dict_cars_list if dic_car.get("brand") == 'Toyota']
    return Toyota_cars

def get_Dacia_cars(dict_cars_list):

    Dacia_cars = [dic_car for dic_car in dict_cars_list if dic_car.get("brand") == 'Dacia']
    return Dacia_cars

def get_Mercedes_cars(dict_cars_list):

    Mercedes_cars = [dic_car for dic_car in dict_cars_list if dic_car.get("brand") == 'Mercedes']
    return Mercedes_cars

def get_Golf_cars(dict_cars_list):

    Golf_cars = [dic_car for dic_car in dict_cars_list if dic_car.get("brand") == 'Golf']
    return Golf_cars

def get_Renault_cars(dict_cars_list):

    Renault_cars = [dic_car for dic_car in dict_cars_list if dic_car.get("brand") == 'Renault']
    return Renault_cars

def get_Ford_cars(dict_cars_list):

    Ford_cars = [dic_car for dic_car in dict_cars_list if dic_car.get("brand") == 'Ford']
    return Ford_cars

def get_Chevrolet_cars(dict_cars_list):

    Chevrolet_cars = [dic_car for dic_car in dict_cars_list if dic_car.get("brand") == 'Chevrolet']
    return Chevrolet_cars
