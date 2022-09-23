# n = input("Enter a number: ")
# n = int(n)


def is_prime(n):
    n = int(n)
    if type(n) == int:
        for a in range(2, n):
            if n % a == 0:
                return False
        return True

# print(is_prime(n))