# n = input("Enter a number: ")
# n_div = int(n)

def div(n_div):
    n_div = int(n_div)
    divisors = [1]
    for i in range(2, n_div):
        if (n_div % i) == 0:
            divisors.append(i)
    return divisors


# print(div(n_div))