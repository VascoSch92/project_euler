from utils.functions import is_prime


class Problem7:
    TITLE = '10001st prime'
    DESCRIPTION = "By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime \n " \
                  "is 13.What is the 10 001st prime number?"

    def answer(self) -> int:
        prime_number_count = 0
        number = 1

        while prime_number_count < 10_001:
            number += 1

            if is_prime(number):
                prime_number_count += 1

        return number
