from utils.functions import is_prime
from itertools import permutations


class Problem41:
    TITLE = 'Pandigital prime'
    DESCRIPTION = "We shall say that an n-digit number is pandigital if it makes use of all the digits 1 \n " \
                  "to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime. \n  " \
                  "What is the largest n-digit pandigital prime that exists?"

    def answer(self) -> int:

        for j in range(9, 4, -1):
            digits = ''.join([str(digit) for digit in range(1, j)])
            n_pandigital_numbers = sorted([''.join(d) for d in permutations(digits)], reverse=True)
            for number in n_pandigital_numbers:
                if is_prime(number=int(number)):
                    return int(number)
