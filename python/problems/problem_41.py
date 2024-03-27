from python.utils.functions import is_prime
from itertools import permutations


class Problem41:
    TITLE = "Pandigital prime"
    DESCRIPTION = "https://projecteuler.net/problem=41"

    def answer(self) -> int:
        for j in range(9, 4, -1):
            digits = "".join([str(digit) for digit in range(1, j)])
            n_pandigital_numbers = sorted(
                ["".join(d) for d in permutations(digits)], reverse=True
            )
            for number in n_pandigital_numbers:
                if is_prime(number=int(number)):
                    return int(number)
