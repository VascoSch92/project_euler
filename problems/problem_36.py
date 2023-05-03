from utils.functions import is_palindrome


class Problem36:
    TITLE = 'Double-base palindromes'
    DESCRIPTION = "The decimal number, 585 = 1001001001 (binary), is palindromic in both bases. \n" \
                  "Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.\n" \
                  "(Please note that the palindromic number, in either base, may not include leading zeros.)"

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
