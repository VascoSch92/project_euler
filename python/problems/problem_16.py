from python.utils.functions import sum_of_digits


class Problem16:
    TITLE = "Power digit sum"
    DESCRIPTION = "https://projecteuler.net/problem=16"

    def answer(self) -> int:
        return sum_of_digits(2**1000)
