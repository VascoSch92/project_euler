import string
from math import isqrt, gcd, factorial
from typing import List


def alphabetic_score(word: str) -> int:
    letters = string.ascii_lowercase
    return sum([letters.index(letter) + 1 for letter in word.lower()])


def euler_totient_function(number: int) -> int:
    if number == 1:
        return 0
    output = 1
    for num in range(2, number + 1):
        if gcd(number, num) == 1:
            output += 1
    return output


def is_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]


def is_pandigital(number: int, digits: str) -> bool:
    return sorted(str(number)) == digits


def is_prime(number: int) -> bool:
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
    index = (- 1 + (1 + 8 * number) ** (1 / 2)) / 2
    return index - int(index) == 0


def is_a_pentagonal_number(number: int) -> bool:
    index = (1 + (1 + 24 * number) ** (1 / 2)) / 6
    return index - int(index) == 0


def is_a_hexagonal_number(number: int) -> bool:
    index = (1 + (1 + 8 * number) ** (1 / 2)) / 4
    return index - int(index) == 0


def max_path_sum_triangle(triangle: List[List[int]]) -> int:
    assert [len(row) for row in triangle] == [j for j in range(1, len(triangle) + 1)]

    depth_triangle = len(triangle)
    for idx_level in range(depth_triangle - 2, -1, -1):
        for idx in range(len(triangle[idx_level])):
            triangle[idx_level][idx] = max(
                triangle[idx_level][idx] + triangle[idx_level + 1][idx],
                triangle[idx_level][idx] + triangle[idx_level + 1][idx + 1]
            )
    return triangle[0][0]


def number_of_divisors(number: int) -> int:
    number_divisors = 0

    for divisor in range(1, isqrt(number) + 1):
        if number % divisor == 0:
            number_divisors += 1
            if divisor != number / divisor:
                number_divisors += 1

    return number_divisors


def sum_factorial_digits(number: int) -> int:
    summation = 0
    for d in str(number):
        summation += factorial(int(d))

    return summation


def sum_of_digits(number: int) -> int:
    if number:
        return sum([int(n) for n in str(number).replace('0', '')])
    else:
        return 0


def triangular_number(number: int) -> int:
    return number * (number + 1) // 2


def pentagonal_number(number: int) -> int:
    return number * (3 * number - 1) // 2


def reverse_and_sum(number: int) -> int:
    return int(number) + int(str(number)[::-1])
