from typing import List
from python.utils.functions import alphabetic_score
from pathlib import Path


class Problem22:
    TITLE = "Names scores"
    DESCRIPTION = "https://projecteuler.net/problem=22"

    def answer(self) -> int:
        path_to_file = Path.cwd()
        names = self.extract_names_from_text(path=path_to_file / "files/problem_22.txt")

        total_name_scores = 0
        for position, name in enumerate(names, start=1):
            total_name_scores += position * alphabetic_score(name)

        return total_name_scores

    @staticmethod
    def extract_names_from_text(path: Path) -> List[str]:
        with open(path) as file_txt:
            names = []
            for line in file_txt.readlines():
                names.extend(line.split(","))

            return sorted([name.replace('"', "") for name in names])
