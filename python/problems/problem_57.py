class Problem57:
    TITLE = "Square root convergents"
    DESCRIPTION = "https://projecteuler.net/problem=57"

    def answer(self) -> int:
        number_of_fractions = 0
        expansion_level = 1
        p_n_2, p_n_1 = 0, 1

        while expansion_level < 1_000:
            p_n_1, p_n_2 = 2 * p_n_1 + p_n_2, p_n_1

            numerator = p_n_2 + p_n_1
            denominator = p_n_1

            if len(str(numerator)) > len(str(denominator)):
                number_of_fractions += 1

            expansion_level += 1

        return number_of_fractions
