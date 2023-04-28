class Problem92:
    TITLE = 'Square digit chains'
    DESCRIPTION = "A number chain is created by continuously adding the square of the digits in a number \n" \
                  "to form a new number until it has been seen before. Any chain that arrives at 1 or 89 \n" \
                  " will become stuck in an endless loop. How many starting numbers below ten million will\n" \
                  " arrive at 89?"

    def answer(self) -> int:
        numbers_ending_with_1 = set()
        numbers_ending_with_89 = set()

        for start_number in range(2, 10_000_000):
            number = start_number

            while True:
                number = self.sum_square_of_the_digits(number=number)

                if number in numbers_ending_with_89 or number == 89:
                    numbers_ending_with_89.add(start_number)
                    break
                if number in numbers_ending_with_1 or number == 1:
                    numbers_ending_with_1.add(start_number)
                    break
        return len(numbers_ending_with_89)

    @staticmethod
    def sum_square_of_the_digits(number: int) -> int:
        summation = 0
        for d in str(number).replace('0', ''):
            summation += int(d) ** 2
        return summation
