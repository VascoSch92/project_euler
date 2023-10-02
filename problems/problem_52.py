class Problem52:
    TITLE = 'Permuted Multiples'
    DESCRIPTION = 'https://projecteuler.net/problem=52'

    def answer(self) -> int:
        x = 1
        while True:
            sorted_x = sorted(str(x))

            if sorted(str(2 * x)) == sorted_x:
                if sorted(str(3 * x)) == sorted_x:
                    if sorted(str(4 * x)) == sorted_x:
                        if sorted(str(5 * x)) == sorted_x:
                            if sorted(str(6 * x)) == sorted_x:
                                return x
            x += 1
