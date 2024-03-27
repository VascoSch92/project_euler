from math import gcd


class Problem33:
    TITLE = "Digit cancelling fractions"
    DESCRIPTION = "https://projecteuler.net/problem=33"

    def answer(self) -> int:
        number_of_examples = 0
        numerator = 10
        product_of_numerators, product_of_denominators = 1, 1

        while number_of_examples < 4:
            numerator_first_digit = numerator // 10
            numerator_second_digit = numerator % 10
            if numerator_second_digit > numerator_first_digit:
                for denominator in range(
                    numerator_second_digit * 10 + 1, numerator_second_digit * 10 + 10
                ):
                    denominator_second_digit = denominator % 10

                    if (
                        numerator / denominator
                        == numerator_first_digit / denominator_second_digit
                    ):
                        product_of_numerators *= numerator
                        product_of_denominators *= denominator
                        number_of_examples += 1
            numerator += 1

        greats_common_divisor = gcd(product_of_numerators, product_of_denominators)

        return int(product_of_denominators / greats_common_divisor)
