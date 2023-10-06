from utils.functions import sum_factorial_digits


class Problem34:
    TITLE = 'Digit factorials'
    DESCRIPTION = 'https://projecteuler.net/problem=34'

    def answer(self) -> int:
        sum_numbers = 0

        for number in range(10, 500_000):
            if number == sum_factorial_digits(number=number):
                sum_numbers += number

        return sum_numbers
