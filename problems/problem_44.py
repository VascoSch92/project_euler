from utils.functions import is_a_pentagonal_number


class Problem44:
    TITLE = 'Pentagon numbers'
    DESCRIPTION = 'https://projecteuler.net/problem=44'

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
