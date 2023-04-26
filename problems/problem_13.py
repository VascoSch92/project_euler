import numpy as np


class Problem13:
    TITLE = 'Large sum'
    DESCRIPTION = 'Work out the first ten digits of the sum of the following one-hundred 50-digit \n' \
                  ' numbers (problem_13.txt).'

    def answer(self) -> int:
        number = self.extract_number_from_text(path='/Users/argo/git/project_euler/files/problem_13.txt')
        large_sum = np.sum(number)
        return str(large_sum)[:10]

    @staticmethod
    def extract_number_from_text(path: str) -> np.ndarray:
        with open(path) as file_txt:
            return np.array([int(line.strip()) for line in file_txt.readlines()])
