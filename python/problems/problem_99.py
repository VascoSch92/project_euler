from typing import List
from math import log
from pathlib import Path


class Problem99:
    TITLE = "Largest Exponential"
    DESCRIPTION = "https://projecteuler.net/problem=99"

    def answer(self) -> int:
        path_to_file = Path.cwd()
        base_exponent_pairs = self.extract_bases_and_exponents_from_text_file(
            path=path_to_file / "files/problem_99.txt"
        )

        max_log = -float("inf")
        line_number = 0
        for i, base_and_exp in enumerate(base_exponent_pairs, start=1):
            base, exp = base_and_exp
            pair_log = int(exp) * log(int(base))

            if pair_log > max_log:
                max_log = pair_log
                line_number = i

        return line_number

    @staticmethod
    def extract_bases_and_exponents_from_text_file(path: Path) -> List:
        with open(path) as file_txt:
            bases_and_exponents = [
                tuple(line.strip().split(",")) for line in file_txt.readlines()
            ]

        return bases_and_exponents
