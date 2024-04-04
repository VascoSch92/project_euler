from python.utils.functions import sum_of_digits


class Problem65:
    TITLE = "Convergents of e"
    DESCRIPTION = "https://projecteuler.net/problem=65"

    def answer(self) -> int:
        numerator_i_1, numerator_i, quotient_i = 1, 2, 1
        convergent, step, period = 1, 1, 2

        while convergent < 100:
            numerator_i, numerator_i_1 = (
                numerator_i * quotient_i + numerator_i_1,
                numerator_i,
            )

            convergent += 1
            if step == 1:
                step += 1
                quotient_i = period
                period += 2
            elif step == 2:
                step += 1
                quotient_i = 1
            elif step == 3:
                step = 1
                quotient_i = 1

        return sum_of_digits(number=numerator_i)
