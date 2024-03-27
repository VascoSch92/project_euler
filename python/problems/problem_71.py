class Problem71:
    TITLE = "Ordered fractions"
    DESCRIPTION = "https://projecteuler.net/problem=71"

    def answer(self) -> int:
        for denominator in range(1_000_000, 2, -1):
            if denominator % 7 == 0:
                return 3 * (denominator // 7) - 1
