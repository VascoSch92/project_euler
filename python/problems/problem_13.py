import numpy as np
from pathlib import Path


class Problem13:
    TITLE = "Large sum"
    DESCRIPTION = "https://projecteuler.net/problem=13"

    def answer(self) -> str:
        path_to_file = Path.cwd()
        number = self.extract_number_from_text(
            path=path_to_file / "files/problem_13.txt"
        )
        large_sum = np.sum(number)
        return str(large_sum)[:10]

    @staticmethod
    def extract_number_from_text(path: Path) -> np.ndarray:
        with open(path) as file_txt:
            return np.array([int(line.strip()) for line in file_txt.readlines()])
