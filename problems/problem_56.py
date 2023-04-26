from utils.functions import sum_of_digits


class Problem56:
    TITLE = 'Powerful digit sum'
    DESCRIPTION = "A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost \n" \
                  "unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the\n " \
                  "digits in each number is only 1. Considering natural numbers of the form, ab, where a, b < 100,\n" \
                  " what is  the maximum digital sum?"

    def answer(self) -> int:
        maximal_digit_sum = 0

        for a in range(10, 100):
            for b in range(10, 100):
                maximal_digit_sum = max(maximal_digit_sum, sum_of_digits(a ** b))

        return maximal_digit_sum
