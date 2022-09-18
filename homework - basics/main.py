# ex 1
def my_function(*args, **kwargs):
    suma = 0

    for arg in args:
        if type(arg) == int or type(arg) == float:
            suma =suma + arg
    else:
        return suma


print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2))

# ex 2.1
def get_sum(n):
    if n == 0:
        return 0

    return n + get_sum(n-1)

print(get_sum(10))

# ex 2.2
def sum_even_n(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return n + sum_even_n(n-2)
    else:
        return sum_even_n(n-1)

print(sum_even_n(10))

# ex 2.3
def sum_odd_n(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return sum_odd_n(n-1)
    else:
        return n + sum_odd_n(n-2)

print(sum_odd_n(10))

# # ex 3.1
user_input = input("Please enter the number here -> ")

try:
    int(user_input)
    insert_value = user_input
except ValueError:
    insert_value = 0

print(insert_value)