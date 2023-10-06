from utils.functions import is_palindrome


class Problem4:
    TITLE = 'Largest palindrome product'
    DESCRIPTION = 'https://projecteuler.net/problem=4'

    def answer(self) -> int:
        answer = float('-inf')
        for num1 in reversed(range(100, 999)):
            for num2 in reversed(range(100, 999)):
                if is_palindrome(num1*num2):
                    answer = max(answer, num1*num2)

        return answer
