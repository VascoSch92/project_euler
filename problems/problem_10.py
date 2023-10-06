from utils.functions import is_prime


class Problem10:
    TITLE = 'Summation of primes'
    DESCRIPTION = 'https://projecteuler.net/problem=10'

    def answer(self) -> int:
        summation_of_primes = 2

        for number in range(3, 2_000_000, 2):
            if is_prime(number):
                summation_of_primes += number

        return summation_of_primes
