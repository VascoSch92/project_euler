class Problem29:
    TITLE = "Distinct powers"
    DESCRIPTION = "https://projecteuler.net/problem=29"

    def answer(self) -> int:
        distinct_terms = set()

        for a in range(2, 101):
            for b in range(2, 101):
                distinct_terms.add(a**b)

        return len(distinct_terms)
