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


def is_a_triangular_number(number: int) -> bool:
    if number == 0 or number == 1:
        return True

    triangular_sum = 0

    for n in range(1, number // 2 + 2):
        triangular_sum += n

        if triangular_sum == number:
            return True

    return False


def number_of_divisors(number: int) -> int:
    number_divisors = 0

    for divisor in range(1, isqrt(number) + 1):
        if number % divisor == 0:
            number_divisors += 1
            if divisor != number / divisor:
                number_divisors += 1

    return number_divisors


def sum_of_digits(number: int) -> int:
    return sum([int(n) for n in str(number)])


def triangular_number(number: int) -> int:
    return number * (number + 1) // 2
