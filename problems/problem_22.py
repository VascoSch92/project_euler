from typing import List
from utils.functions import alphabetic_score


class Problem22:
    TITLE = 'Names scores'
    DESCRIPTION = "Using problem_22.txt, a 46K text file containing over five-thousand first names, begin by \n " \
                  "sorting it into alphabetical order. Then working out the alphabetical value for each name, \n" \
                  "multiply this value by its alphabetical position in the list to obtain a name score. For example,\n" \
                  " when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,\n" \
                  " is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.\n" \
                  "What is the total of all the name scores in the file?"

    def answer(self) -> int:
        names = self.extract_names_from_text(path='/Users/argo/git/project_euler/files/problem_22.txt')

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
