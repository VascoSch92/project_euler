from typing import List


class Problem28:
    TITLE = 'Number spiral diagonals'
    DESCRIPTION = 'https://projecteuler.net/problem=28'

    def answer(self) -> int:
        return sum(self.diagonal_sequence(length_side=1001))

    @staticmethod
    def diagonal_sequence(length_side: int) -> List[int]:
        number_of_terms = 2 * length_side - 2
        diagonal_sequence = [1]

        count = 0
        add_term = 2
        while len(diagonal_sequence) <= number_of_terms:
            if count == 4:
                count = 0
                add_term += 2
            diagonal_sequence.append(diagonal_sequence[-1] + add_term)
            count += 1
        return diagonal_sequence
