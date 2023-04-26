from typing import List
import numpy as np


class Problem8:
    TITLE = 'Largest product in a series'
    DESCRIPTION = "Find the thirteen adjacent digits in the 1000-digit number (in problem_8.txt) that have the" \
                  " greatest product. What is the value of this product?"

    def answer(self) -> int:
        series = self.extract_series_from_text(path='/Users/argo/git/project_euler/files/problem_8.txt')

        greatest_product = float('-inf')
        for idx in range(0, len(series) - 13):
            product = np.prod(series[idx: idx + 13])
            greatest_product = max(greatest_product, product)

        return greatest_product

    @staticmethod
    def extract_series_from_text(path: str) -> np.ndarray:
        with open(path) as file_txt:
            lines = [line.strip() for line in file_txt.readlines()]

            series = []
            for line in lines:
                for number in list(line):
                    series.append(int(number))

            return np.array(series)
