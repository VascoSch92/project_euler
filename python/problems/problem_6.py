import numpy as np


class Problem6:
    TITLE = "Sum square difference"
    DESCRIPTION = "https://projecteuler.net/problem=6"

    def answer(self) -> int:
        numbers = np.array(range(1, 101))

        sum_of_the_squares = np.sum(numbers**2)
        square_of_the_sum = np.sum(numbers) ** 2

        return square_of_the_sum - sum_of_the_squares
