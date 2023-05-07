import numpy as np
from math import gcd


class Problem33:
    TITLE = 'Digit cancelling fractions'
    DESCRIPTION = "The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to\n " \
                  " simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by \n " \
                  " cancelling the 9s. We shall consider fractions like, 30/50 = 3/5, to be trivial examples.\n" \
                  " There are exactly four non-trivial examples of this type of fraction, less than one in value,\n" \
                  " and containing two digits in the numerator and denominator. If the product of these four\n" \
                  " fractions is given in its lowest common terms, find the value of the denominator."

    def answer(self) -> int:
        number_of_examples = 0
        numerator = 10
        product_of_numerators, product_of_denominators = 1, 1

        while number_of_examples < 4:
            numerator_first_digit = numerator // 10
            numerator_second_digit = numerator % 10
            if numerator_second_digit > numerator_first_digit:
                for denominator in range(numerator_second_digit * 10 + 1, numerator_second_digit * 10 + 10):
                    denominator_second_digit = denominator % 10

                    if numerator / denominator == numerator_first_digit / denominator_second_digit:
                        product_of_numerators *= numerator
                        product_of_denominators *= denominator
                        number_of_examples += 1
            numerator += 1

        greats_common_divisor = gcd(product_of_numerators, product_of_denominators)

        return int(product_of_denominators / greats_common_divisor)
