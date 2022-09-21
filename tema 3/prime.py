# n = int(input("Enter a number: "))

def is_prime(n):
    for a in range(2, n):
        if n % a == 0:
            return False

    return True


# print(is_prime(n))