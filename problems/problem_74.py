from typing import Set

from utils.functions import sum_factorial_digits


class Problem74:
    TITLE = 'Digit factorial chains'

    def answer(self) -> int:
        number_of_chains = 0

        for starting_number in range(1_000_000):
            if len(self.digit_factorial_chain(number=starting_number)) == 60:
                number_of_chains += 1
        return number_of_chains

    def digit_factorial_chain(self, number: int) -> Set:
        chain = {number}
        number = sum_factorial_digits(number=number)

        while number not in chain:
            chain.add(number)
            number = sum_factorial_digits(number=number)

        return chain
