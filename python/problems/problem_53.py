from math import comb as binomial


class Problem53:
    TITLE = "Combinatoric Selections"
    DESCRIPTION = "https://projecteuler.net/problem=53"

    def answer(self) -> int:
        answer = 0

        for n in range(1, 101):
            for r in range(n + 1):
                if binomial(n, r) > 1_000_000:
                    answer += 1
        return answer
