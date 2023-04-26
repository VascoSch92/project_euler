from math import sqrt


class Problem9:
    TITLE = 'Special Pythagoren triplet'
    DESCRIPTION = "A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, \n " \
                  "a**2 + b**2 = c**2 \n " \
                  "There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc."

    def answer(self) -> int:

        for a in range(999):
            for b in range(a + 1, 1_000):
                c = sqrt(a ** 2 + b ** 2)
                if b < c and a + b + c == 1000:
                    return int(a * b * c)
