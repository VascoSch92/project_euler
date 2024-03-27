class Problem48:
    TITLE = "Self powers"
    DESCRIPTION = "https://projecteuler.net/problem=18"

    def answer(self) -> int:
        series = 0

        for number in range(1, 1_001):
            series += number**number
            series = int(str(series)[-10:])

        return series
