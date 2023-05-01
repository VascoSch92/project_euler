from math import isqrt


class Problem23:
    TITLE = 'Non-abundant sums'
    DESCRIPTION = "A perfect number is a number for which the sum of its proper divisors is exactly equal \n " \
                  "to the number. For example, the sum of the proper divisors of 28 is 28,\n " \
                  "which means that 28 is a perfect number. A number n is called deficient if the sum of its proper\n " \
                  "divisors is less than n and it is called abundant if this sum exceeds n. As 12 is the smallest\n " \
                  "abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of \n " \
                  "two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater\n " \
                  "than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot\n " \
                  "be reduced any further by analysis even though it is known that the greatest number that cannot\n " \
                  "be expressed as the sum of two abundant numbers is less than this limit. \n" \
                  "Find the sum of all the positive integers which cannot be written as the sum of two \n " \
                  "abundant numbers."

    def answer(self) -> int:
        abundant_numbers = self.list_abundant_numbers(start=12, stop=28_124)

        numbers_that_are_sum_of_2_abundant_numbers = set()
        for idx, num1 in enumerate(abundant_numbers):
            for num2 in abundant_numbers[idx:]:
                if num1 + num2 <= 28_123:
                    numbers_that_are_sum_of_2_abundant_numbers.add(num1 + num2)

        return self.sum_from_1_to_n(n=28_123) - sum(list(numbers_that_are_sum_of_2_abundant_numbers))

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
