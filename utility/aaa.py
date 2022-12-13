my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def every_third_number(lista):
    return [lista[i] for i in range(0, len(lista), 3)]

print(every_third_number(my_list))