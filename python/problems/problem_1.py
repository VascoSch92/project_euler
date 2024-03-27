class Problem1:
    TITLE = "Multiples of 3 or 5"
    DESCRIPTION = "https://projecteuler.net/problem=1"

    def answer(self) -> int:
        sum_of_multiples = 0

        for number in range(1, 1000):
            if number % 3 == 0 or number % 5 == 0:
                sum_of_multiples += number

        return sum_of_multiples
