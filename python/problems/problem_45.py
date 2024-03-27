from python.utils.functions import (
    is_a_pentagonal_number,
    is_a_hexagonal_number,
)


class Problem45:
    TITLE = "Triangular, pentagonal, and hexagonal"
    DESCRIPTION = "https://projecteuler.net/problem=45"

    def answer(self) -> int:
        index = 286

        while True:
            triangular_number = self.T(index=index)
            if is_a_pentagonal_number(
                number=triangular_number
            ) and is_a_hexagonal_number(number=triangular_number):
                return triangular_number
            index += 1

    def T(self, index: int) -> int:
        return index * (3 * index - 1) // 2
