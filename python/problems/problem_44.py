from python.utils.functions import is_a_pentagonal_number


class Problem44:
    TITLE = "Pentagon numbers"
    DESCRIPTION = "https://projecteuler.net/problem=44"

    def answer(self) -> int:
        idx_1 = 2

        while True:
            for idx_2 in range(1, idx_1):
                p_1, p_2 = (
                    self.pentagon_number(index=idx_1),
                    self.pentagon_number(index=idx_2),
                )
                if is_a_pentagonal_number(number=p_1 - p_2):
                    if is_a_pentagonal_number(number=p_1 + p_2):
                        return p_1 - p_2
            idx_1 += 1

    @staticmethod
    def pentagon_number(index: int) -> int:
        return index * (3 * index - 1) // 2
