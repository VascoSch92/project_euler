from typing import List
from utils.functions import max_path_sum_triangle


class Problem18:
    TITLE = 'Maximum path sum I'
    DESCRIPTION = 'https://projecteuler.net/problem=18'

    def answer(self) -> int:
        triangle = self.read_triangle_from_txt(path='files/problem_18.txt')

        return max_path_sum_triangle(triangle=triangle)

    @staticmethod
    def read_triangle_from_txt(path: str) -> List[List[int]]:
        with open(path) as file_txt:
            triangle = []
            for line in file_txt.readlines():
                line = line.strip().split(' ')
                triangle.append([int(number) for number in line])
        return triangle
