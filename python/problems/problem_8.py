import numpy as np
from pathlib import Path
from typing import Union


class Problem8:
    TITLE = "Largest product in a series"
    DESCRIPTION = "https://projecteuler.net/problem=8"

    def answer(self) -> int:
        path_to_file = Path.cwd()
        series = self.extract_series_from_text(
            path=path_to_file / "files/problem_8.txt"
        )

        greatest_product = float("-inf")
        for idx in range(0, len(series) - 13):
            product = np.prod(series[idx : idx + 13])
            greatest_product = max(greatest_product, product)

        return greatest_product

    @staticmethod
    def extract_series_from_text(path: Union[Path, str]) -> np.ndarray:
        with open(path) as file_txt:
            lines = [line.strip() for line in file_txt.readlines()]

            series = []
            for line in lines:
                for number in list(line):
                    series.append(int(number))

            return np.array(series)
