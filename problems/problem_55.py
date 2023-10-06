from utils.functions import is_palindrome, reverse_and_sum


class Problem55:
    TITLE = 'Lychrel Numbers'
    DESCRIPTION = 'https://projecteuler.net/problem=55'

    def answer(self) -> int:
        total_number_of_lycherel_numbers = 0

        for number in range(1, 10001):
            if self.is_lycherel(number=number):
                total_number_of_lycherel_numbers += 1

        return total_number_of_lycherel_numbers

    @staticmethod
    def is_lycherel(number: int):
        for _ in range(50):
            number = reverse_and_sum(number=number)
            if is_palindrome(number=number):
                return False
        return True
