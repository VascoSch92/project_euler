from python.utils.functions import is_a_square


class Problem46:
    TITLE = "Goldbachs Other Conjecture"
    DESCRIPTION = "https://projecteuler.net/problem=46"

    def answer(self) -> int:
        prime_list = []
        odd_composite = 9
        while True:
            is_a_counterexample = True
            for prime in prime_list:
                if prime >= odd_composite:
                    break
                else:
                    if is_a_square((odd_composite - prime) / 2):
                        is_a_counterexample = False

            if is_a_counterexample:
                return odd_composite
            else:
                if odd_composite + 2 not in prime_list:
                    ...
