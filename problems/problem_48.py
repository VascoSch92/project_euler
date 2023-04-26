class Problem48:
    TITLE = 'Self powers'
    DESCRIPTION = "The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.\n " \
                  "Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000."

    def answer(self) -> int:
        series = 0

        for number in range(1, 1_001):
            series += number ** number
            series = int(str(series)[-10:])

        return series
