from utils.functions import is_prime


class Problem69:
    TITLE = 'Totient maximum'
    DESCRIPTION = 'https://projecteuler.net/problem=69'

    def answer(self) -> int:
        n, number = 1, 0

        while n * number <= 1_000_000:
            number += 1

            if is_prime(number=number):
                n *= number

        return n
