# n = input("Enter a number : ")
# n_dig = int(n)

def nr_digits(n_dig):
    n_dig = int(n_dig)
    count = 0
    while n_dig != 0:
        count = count + 1
        n_dig //= 10
    return count


# print(nr_digits(n_dig))