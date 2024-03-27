from python.utils.functions import (
    triangular_number,
    number_of_divisors,
)


class Problem12:
    TITLE = "Highly divisible triangular number"
    DESCRIPTION = "https://projecteuler.net/problem=12"

    def answer(self) -> int:
        t_n = triangular_number(n := 500)

        while number_of_divisors(t_n) < 500:
            n += 1
            t_n = triangular_number(n)

        return t_n
