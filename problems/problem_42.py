from typing import List
from utils.functions import alphabetic_score, is_a_triangular_number


class Problem42:
    TITLE = 'Coded triangle numbers'
    DESCRIPTION = "The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first\n" \
                  "ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ... By converting each letter \n " \
                  "in a word to a number corresponding to its alphabetical position and adding these values we \n " \
                  "form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word\n " \
                  "value is a triangle number then we shall call the word a triangle word. \n " \
                  "Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly \n " \
                  "two-thousand common English words, how many are triangle words?"

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
