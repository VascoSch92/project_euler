from utils.functions import is_prime


class Problem69:
    TITLE = 'Totient maximum'
    DESCRIPTION = "Euler's Totient function phi, (sometimes called the phi function), is defined as \n" \
                  "the number of positive integers not exceeding which are relatively prime to . \n" \
                  "For example, as 1, 2, 4, 5, 7, and 8, are all less than or equal to nine and \n" \
                  "relatively prime to nine, phi(9) = 6. Find the value of n <= 1_000_000 for which \n" \
                  "n/phi(n) is a maximum."

    def answer(self) -> int:
        n, number = 1, 0

        while n * number <= 1_000_000:
            number += 1

            if is_prime(number=number):
                n *= number

        return n
