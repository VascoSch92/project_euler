from utils.functions import is_a_pentagonal_number, is_a_hexagonal_number


class Problem45:
    TITLE = 'Triangular, pentagonal, and hexagonal'
    DESCRIPTION = "Triangle, pentagonal, and hexagonal numbers are generated by the following formulae: Tn=n(n+1)/2 \n" \
                  "Pn=n(3n−1)/2, Hn=n(2n−1). It can be verified that T_285 = P_165 = H_143 = 40755. \n" \
                  "Find the next triangle number that is also pentagonal and hexagonal."

    def answer(self) -> int:
        index = 286

        while True:
            triangular_number = self.T(index=index)
            if is_a_pentagonal_number(number=triangular_number) and is_a_hexagonal_number(number=triangular_number):
                return triangular_number
            index += 1

    def T(self, index: int) -> int:
        return index * (3 * index - 1) // 2
