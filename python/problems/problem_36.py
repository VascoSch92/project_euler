from python.utils.functions import is_palindrome


class Problem36:
    TITLE = "Double-core palindromes"
    DESCRIPTION = "https://projecteuler.net/problem=36"

    def answer(self) -> int:
        total = 0

        for number in range(1_000_000):
            if is_palindrome(number=number):
                if is_palindrome(number=self.binary_representation(number=number)):
                    total += number

        return total

    @staticmethod
    def binary_representation(number: int) -> int:
        binary = bin(number)[2:]
        return int(binary)
