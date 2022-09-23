
# n = int(input("Enter an integer:"))
# n_div = int(n)


def max_divisors(n_div):
    n_div = int(n_div)
    largest_divisor = 0
    for i in range(2, n_div):
        if n_div % i == 0:
            largest_divisor = i
    return largest_divisor


# print(max_divisors(n_div))