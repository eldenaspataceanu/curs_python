from palindrome import is_palindrome
from prime import is_prime

my_dict = {}
ex = input('Enter an integer here : ')

while True:
    if ex.isdigit():
        print('Number is int')
        my_dict = {
            "is_palindrome": is_palindrome(ex),
            "is_prime": is_prime(ex)
            # "divisors": [2, 4, 5, 10]
            # "max_divisor": 10,
            # "digits": 2,
        }
        break
    else:
        print('Wrong type, introduce number again')
        ex = input('Enter an integer here : ')
        if ex == "exit" or ex == "quit":
            break
print(my_dict)