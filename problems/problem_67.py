from typing import List
from utils.functions import max_path_sum_triangle


class Problem67:
    TITLE = 'Maximum path sum II'
    DESCRIPTION = 'Find the maximum total from top to bottom in problem_67.txt , a 15K text file containing \n' \
                  ' a triangle with one-hundred rows.'

    def answer(self) -> int:
        triangle = self.read_triangle_from_txt(path='files/problem_67.txt')

        return max_path_sum_triangle(triangle=triangle)

    @staticmethod
    def read_triangle_from_txt(path: str) -> List[List[int]]:
        with open(path) as file_txt:
            triangle = []
            for line in file_txt.readlines():
                line = line.strip().split(' ')
                triangle.append([int(number) for number in line])
        return triangle
