from utils.functions import sum_of_digits


class Problem65:
    TITLE = 'Convergents of e'
    DESCRIPTION = "Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e."

    def answer(self) -> int:
        numerator_i_1 = 1
        numerator_i = 2
        quotient_i = 1

        convergent = 1
        step = 1
        period = 2

        while convergent < 100:
            numerator_i, numerator_i_1 = numerator_i * quotient_i + numerator_i_1, numerator_i

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
