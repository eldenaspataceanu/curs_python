my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_list_sort = sorted(my_list)

print(my_list_sort[::])   # Afiseaza lista ordonata ascendent
print(my_list_sort[::-1])    # Afiseaza lista ordonata descendent
print(my_list_sort[1::2])   # Afiseaza lista cu numere pare
print(my_list_sort[::2])    # Afiseaza lista cu numerele impare
print(my_list_sort[2:10:3]) # Afiseaza lista cu numere ce sunt multipli de 3