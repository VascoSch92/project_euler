from utils.functions import is_a_pentagonal_number


class Problem44:
    TITLE = 'Pentagon numbers'
    DESCRIPTION = "Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal\n" \
                  "numbers are: 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ... It can be seen that \n " \
                  "P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal. \n " \
                  "Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference \n " \
                  "are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?"

    def answer(self) -> int:
        idx_1 = 2

        while True:
            for idx_2 in range(1, idx_1):
                p_1, p_2 = self.P(n=idx_1), self.P(n=idx_2)
                if is_a_pentagonal_number(number=p_1 - p_2):
                    if is_a_pentagonal_number(number=p_1 + p_2):
                        return p_1 - p_2
            idx_1 += 1

    @staticmethod
    def P(n: int) -> int:
        return n * (3 * n - 1) // 2