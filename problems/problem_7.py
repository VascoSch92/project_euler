from utils.functions import is_prime


class Problem7:
    TITLE = '10001st prime'
    DESCRIPTION = 'https://projecteuler.net/problem=7'

    def answer(self) -> int:
        prime_number_count = 0
        number = 1

        while prime_number_count < 10_001:
            number += 1

            if is_prime(number):
                prime_number_count += 1

        return number
