from math import factorial
from utils.functions import sum_of_digits


class Problem20:
    TITLE = 'Factorial digit sum'
    DESCRIPTION = 'https://projecteuler.net/problem=20'

    def answer(self) -> int:
        return sum_of_digits(factorial(100))
