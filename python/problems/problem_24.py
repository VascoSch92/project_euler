from itertools import permutations


class Problem24:
    TITLE = "Lexicographic permutations"
    DESCRIPTION = "https://projecteuler.net/problem=24"

    def answer(self) -> str:
        digits = "0123456789"
        lexicogaphic_permutation = [p for p in permutations(digits)]

        return "".join([d for d in lexicogaphic_permutation[999_999]])
