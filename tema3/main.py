from palindrome import palindrome
from prime import is_prime
from divisors import div
from max_div import max_divisors
from digits import nr_digits

my_dict = {}
ex = input('Enter an integer here : ')

while True:
    if ex.isdigit():
        print('Number is int')
        my_dict = {
            "is_palindrome": palindrome(ex),
            "is_prime": is_prime(ex),
            "divisors": div(ex),
            "max_divisor": max_divisors(ex),
            "digits": nr_digits(ex)
        }
        break
    else:
        print('Wrong type, introduce number again')
        ex = input('Enter an integer here : ')
        if ex == "exit" or ex == "quit":
            break
print(my_dict)