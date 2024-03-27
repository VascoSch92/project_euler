from python.utils.functions import is_prime


class Problem3:
    TITLE = "Largest prime factor"
    DESCRIPTION = "https://projecteuler.net/problem=3"

    def answer(self) -> int:
        number = 600_851_475_143
        divisor = 2

        while not is_prime(number):
            if number % divisor == 0:
                number //= divisor
            elif divisor + 1 == number:
                return number
            else:
                divisor += 1

        return number
