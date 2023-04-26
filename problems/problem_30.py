class Problem30:
    TITLE = 'Digit fifth powers'
    DESCRIPTION = "Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."

    def answer(self) -> int:
        summation = 0

        for number in range(32, 250_000):
            if self.is_sum_of_fifth_powers_of_digits(number):
                summation += number

        return summation

    @staticmethod
    def is_sum_of_fifth_powers_of_digits(number: int) -> bool:
        return number == sum([int(d) ** 5 for d in str(number).replace('0', '')])
