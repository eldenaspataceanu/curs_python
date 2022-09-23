# n = input("Enter a number: ")


def palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False

# print(palindrone(n))