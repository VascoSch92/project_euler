from math import isqrt


class Problem21:
    TITLE = 'Amicable numbers'
    DESCRIPTION = 'https://projecteuler.net/problem=21'

    def answer(self) -> int:
        sum_amicable_numbers = 0

        for number in range(10_001):
            d_number = self.d(number)
            if d_number != number == self.d(d_number):
                sum_amicable_numbers += number

        return sum_amicable_numbers

    @staticmethod
    def d(number: int) -> int:
        if number < 2:
            return 0

        sum_of_proper_divisors = 1
        for divisor in range(2, isqrt(number) + 1):
            if number % divisor == 0:
                sum_of_proper_divisors += divisor
                if divisor != number / divisor:
                    sum_of_proper_divisors += number / divisor
        return int(sum_of_proper_divisors)
