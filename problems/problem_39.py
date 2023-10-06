from math import sqrt


class Problem39:
    TITLE = 'Integer right triangles'
    DESCRIPTION = 'https://projecteuler.net/problem=39'

    def answer(self) -> float:
        solutions = {}

        for a in range(500):
            for b in range(500):
                c = sqrt(a ** 2 + b ** 2)
                if int(c) - c == 0:
                    solutions[a + b + c] = solutions.get(a + b + c, 0) + 1

        max_solutions = max(solutions.values())
        return list(filter(lambda x: solutions[x] == max_solutions, solutions))[0]
