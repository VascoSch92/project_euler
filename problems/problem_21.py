from math import isqrt


class Problem21:
    TITLE = 'Amicable numbers'
    DESCRIPTION = "Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide \n" \
                  " evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair \n" \
                  " and each of a and b are called amicable numbers. For example, the proper divisors of 220 are \n" \
                  " 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors \n" \
                  " of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.\n" \
                  "Evaluate the sum of all the amicable numbers under 10000."

    def answer(self) -> int:
        sum_amicable_numbers = 0

        for number in range(10_001):
            d_number = self.d(number)
            if d_number != number == self.d(d_number):
                sum_amicable_numbers += number

        return sum_amicable_numbers

    @staticmethod
    def d(number: int) -> int:
        if number < 2:
            return 0

        sum_of_proper_divisors = 1
        for divisor in range(2, isqrt(number) + 1):
            if number % divisor == 0:
                sum_of_proper_divisors += divisor
                if divisor != number / divisor:
                    sum_of_proper_divisors += number / divisor
        return int(sum_of_proper_divisors)
