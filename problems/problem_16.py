from utils.functions import sum_of_digits


class Problem16:
    TITLE = 'Power digit sum'
    DESCRIPTION = "2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. \n " \
                  "What is the sum of the digits of the number 2**1000?"

    def answer(self) -> int:
        return sum_of_digits(2 ** 1000)
