from math import isqrt


def is_palindrome(number: int) -> bool:
    """ The method return True if the input number is palindrome. Otherwise, False """
    return str(number) == str(number)[::-1]


def is_prime(number: int) -> bool:
    """ The method return True if the input number is prime. Otherwise, False """
    if number <= 3:
        return number > 1
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        for d in range(5, isqrt(number) + 1, 6):
            if number % d == 0 or number % (d + 2) == 0:
                return False
        return True
