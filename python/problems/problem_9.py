from math import sqrt


class Problem9:
    TITLE = "Special Pythagoren triplet"
    DESCRIPTION = "https://projecteuler.net/problem=9"

    def answer(self) -> int:
        for a in range(999):
            for b in range(a + 1, 1_000):
                c = sqrt(a**2 + b**2)
                if b < c and a + b + c == 1000:
                    return int(a * b * c)
