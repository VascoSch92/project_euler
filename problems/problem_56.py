from utils.functions import sum_of_digits


class Problem56:
    TITLE = 'Powerful digit sum'
    DESCRIPTION = 'https://projecteuler.net/problem=56'

    def answer(self) -> int:
        maximal_digit_sum = 0

        for a in range(10, 100):
            for b in range(10, 100):
                maximal_digit_sum = max(maximal_digit_sum, sum_of_digits(a ** b))

        return maximal_digit_sum
