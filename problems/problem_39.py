from math import sqrt


class Problem39:
    TITLE = 'Integer right triangles'
    DESCRIPTION = "If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, \n" \
                  "there are exactly three solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50} For which \n" \
                  "value of p ≤ 1000, is the number of solutions maximised?"

    def answer(self) -> int:
        solutions = {}

        for a in range(500):
            for b in range(500):
                c = sqrt(a ** 2 + b ** 2)
                if int(c) - c == 0:
                    solutions[a + b + c] = solutions.get(a + b + c, 0) + 1

        max_solutions = max(solutions.values())
        return list(filter(lambda x: solutions[x] == max_solutions, solutions))[0]
