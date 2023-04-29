from itertools import permutations


class Problem24:
    TITLE = 'Lexicographic permutations'
    DESCRIPTION = "A permutation is an ordered arrangement of objects. For example, 3124 is one\n" \
                  " possible permutation of the digits 1, 2, 3 and 4. If all of the permutations \n " \
                  "are listed numerically or alphabetically, we call it lexicographic order. The \n " \
                  "lexicographic permutations of 0, 1 and 2 are: 012, 021, 102, 120, 201, 210. \n" \
                  "What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"

    def answer(self) -> int:
        digits = '0123456789'
        lexicogaphic_permutation = [p for p in permutations(digits)]

        return ''.join([d for d in lexicogaphic_permutation[999_999]])
