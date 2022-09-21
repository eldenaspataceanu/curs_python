# n = input("Enter a number: ")


def is_palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False


# print(is_palindrome(n))