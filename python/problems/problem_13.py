import numpy as np


class Problem13:
    TITLE = "Large sum"
    DESCRIPTION = "https://projecteuler.net/problem=13"

    def answer(self) -> str:
        number = self.extract_number_from_text(path="files/problem_13.txt")
        large_sum = np.sum(number)
        return str(large_sum)[:10]

    @staticmethod
    def extract_number_from_text(path: str) -> np.ndarray:
        with open(path) as file_txt:
            return np.array([int(line.strip()) for line in file_txt.readlines()])
