from utils.functions import triangular_number, number_of_divisors


class Problem12:
    TITLE = 'Highly divisible triangular number'
    DESCRIPTION = 'What is the value of the first triangle number to have over five hundred divisors?'

    def answer(self) -> int:
        t_n = triangular_number(n := 500)

        while number_of_divisors(t_n) < 500:
            n += 1
            t_n = triangular_number(n)

        return t_n
