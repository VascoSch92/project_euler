from utils.functions import is_prime


class Problem10:
    TITLE = 'Summation of primes'
    DESCRIPTION = "The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. \n " \
                  "Find the sum of all the primes below two million."

    def answer(self) -> int:
        summation_of_primes = 2

        for number in range(3, 2_000_000, 2):
            if is_prime(number):
                summation_of_primes += number

        return summation_of_primes
