from math import isqrt


class Problem23:
    TITLE = "Non-abundant sums"
    DESCRIPTION = "https://projecteuler.net/problem=23"

    def answer(self) -> int:
        abundant_numbers = self.list_abundant_numbers(start=12, stop=28_124)

        numbers_that_are_sum_of_2_abundant_numbers = set()
        for idx, num1 in enumerate(abundant_numbers):
            for num2 in abundant_numbers[idx:]:
                if num1 + num2 <= 28_123:
                    numbers_that_are_sum_of_2_abundant_numbers.add(num1 + num2)

        return self.sum_from_1_to_n(n=28_123) - sum(
            list(numbers_that_are_sum_of_2_abundant_numbers)
        )

    def list_abundant_numbers(self, start: int, stop: int):
        abundant_numbers = []
        for number in range(start, stop):
            if self.is_abundant(number=number):
                abundant_numbers.append(number)
        return abundant_numbers

    @staticmethod
    def is_abundant(number: int) -> bool:
        sum_of_divisors = 0

        for divisor in range(1, isqrt(number) + 1):
            if number % divisor == 0:
                sum_of_divisors += divisor
                if divisor != number / divisor:
                    sum_of_divisors += number / divisor

        return (sum_of_divisors - number) > number

    @staticmethod
    def sum_from_1_to_n(n: int) -> int:
        return n * (n + 1) // 2
