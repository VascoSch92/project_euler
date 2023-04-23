from utils.functions import is_palindrome


class Problem4:
    TITLE = 'Largest palindrome product'
    DESCRIPTION = "A palindromic number reads the same both ways. The largest palindrome made from the product of \n " \
               " two 2-digit numbers is 9009 = 91 × 99. \n " \
               "Find the largest palindrome made from the product of two 3-digit numbers."

    def answer(self) -> int:
        answer = float('-inf')
        for num1 in reversed(range(100, 999)):
            for num2 in reversed(range(100, 999)):
                if is_palindrome(num1*num2):
                    answer = max(answer, num1*num2)

        return answer
