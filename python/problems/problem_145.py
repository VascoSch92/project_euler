class Problem145:
    TITLE = "Reversible Numbers"
    DESCRIPTION = "https://projecteuler.net/problem=145"

    @property
    def answer(self) -> int:
        """
        It is sufficient to look at the digits to understand how many reversible numbers there are.
        We have the following rules:
            - 1-digit, i.e., number = (a)
                => NO SOLUTION
            - 2-digit, i.e., number = (a,b)
                - a, b are different from 0
                - a + b < 10 and (a + b) % 2 = 1
                => 20 solutions
            - 3-digit, i.e., number = (a,b,c)
                - a, c different from 0
                - a + c > 10 and (a + c) % 2 = 1
                - b + b < 10
                => 5*20 = 100
            - 4-digit, i.e., number = (a,b,c,d)
                - a, d different from 0
                - a + d < 10 and (a + d) % 2 = 1
                - c + b < 10 and (c + b) % 2 = 1
                => 20*30 = 600
            - 5-digit, i.e., number = (a, b, c, d, e)
                => NO SOLUTION
            - 6-digit, i.e., number = (a, b, c, d, e, f)
                - a, f different from 0
                - a + f < 10 and (a + f) % 2 = 1
                - e + b < 10 and (e + b) % 2 = 1
                - c + d < 10 and (d + c) % 2 = 1
                => 20*30*30 = 18_000
            - 7-digit, i.e., number = (a, b, c, d, e, f, g)
                - a, g different from 0
                - g + a > 10 and (g + a) % 2 = 1
                - f + b < 10 and (b + f) % 2 = 0
                - e + c > 10 and (e + c) % 2 = 1
                => 50_000
            - 8-digit, i.e., number = (a, b, c, d, e, f, g, h)
                - a, h different from 0
                - h + a < 10 and (g + a) % 2 = 1
                - g + b < 10 and (b + f) % 2 = 1
                - f + c < 10 and (e + c) % 2 = 1
                - e + d < 10 and (e + d) % 2 = 1
                => 20*30*30*30 = 540_000
            - 9-digit, i.e., number = (a, b, c, d, e, f, g, h, i)
                => NO SOLUTION
        """
        sum_of_reversible_numbers = 0

        # 1-digit
        sum_of_reversible_numbers += 0
        # 2-digit
        sum_of_reversible_numbers += 20
        # 3-digit
        sum_of_reversible_numbers += 100
        # 4-digit
        sum_of_reversible_numbers += 600
        # 5-digit
        sum_of_reversible_numbers += 0
        # 6-digit
        sum_of_reversible_numbers += 18_000
        # 7-digit
        sum_of_reversible_numbers += 50_000
        # 8-digit
        sum_of_reversible_numbers += 540_000
        # 9-digit
        sum_of_reversible_numbers += 0

        return sum_of_reversible_numbers
