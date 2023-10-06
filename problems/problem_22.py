from typing import List
from utils.functions import alphabetic_score


class Problem22:
    TITLE = 'Names scores'
    DESCRIPTION = 'https://projecteuler.net/problem=22'

    def answer(self) -> int:
        names = self.extract_names_from_text(path='files/problem_22.txt')

        total_name_scores = 0
        for position, name in enumerate(names, start=1):
            total_name_scores += position * alphabetic_score(name)

        return total_name_scores

    @staticmethod
    def extract_names_from_text(path: str) -> List[str]:
        with open(path) as file_txt:
            names = []
            for line in file_txt.readlines():
                names.extend(line.split(','))

            return sorted([name.replace('"', '') for name in names])
