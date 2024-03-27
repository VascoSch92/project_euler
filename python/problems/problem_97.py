class Problem97:
    TITLE = "Large Non-Mersenne Prime"
    DESCRIPTION = "https://projecteuler.net/problem=97"

    def answer(self) -> int:
        last_digits = 28433

        for _ in range(7830457):
            last_digits *= 2

            if last_digits > 10_000_000_000:
                last_digits = last_digits % 10_000_000_000

        return last_digits + 1
