from typing import List
from python.utils.functions import max_path_sum_triangle
from pathlib import Path


class Problem67:
    TITLE = "Maximum path sum II"
    DESCRIPTION = "https://projecteuler.net/problem=67"

    def answer(self) -> int:
        path_to_file = Path.cwd()
        triangle = self.read_triangle_from_txt(
            path=path_to_file / "files/problem_67.txt"
        )

        return max_path_sum_triangle(triangle=triangle)

    @staticmethod
    def read_triangle_from_txt(path: Path) -> List[List[int]]:
        with open(path) as file_txt:
            triangle = []
            for line in file_txt.readlines():
                line = line.strip().split(" ")
                triangle.append([int(number) for number in line])
        return triangle
