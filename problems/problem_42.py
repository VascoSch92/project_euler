from typing import List
from utils.functions import alphabetic_score, is_a_triangular_number


class Problem42:
    TITLE = 'Coded triangle numbers'
    DESCRIPTION = 'https://projecteuler.net/problem=42'

    def answer(self) -> int:
        triangle_words = 0

        names = self.extract_names_from_text(path='files/problem_42.txt')

        for name in names:
            if is_a_triangular_number(number=alphabetic_score(word=name)):
                triangle_words += 1
        return triangle_words

    @staticmethod
    def extract_names_from_text(path: str) -> List[str]:
        with open(path) as file_txt:
            names = []
            for line in file_txt.readlines():
                names.extend(line.split(','))

            return sorted([name.replace('"', '') for name in names])
