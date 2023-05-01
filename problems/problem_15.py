from math import comb


class Problem15:
    TITLE = 'Lattice paths'
    DESCRIPTION = "Starting in the top left corner of a 2×2 grid, and only being able to move to the right and\n " \
                  " down, there are exactly 6 routes to the bottom right corner. \n" \
                  "How many such routes are there through a 20×20 grid?"

    def answer(self) -> int:
        """
        The number of NE lattice paths from (0, 0) to (a, b) is equal to the number of combinations of a objects out
        of a set of a+b objects
        """
        return self.number_of_paths(a=20, b=20)

    @staticmethod
    def number_of_paths(a: int, b: int) -> int:
        return comb(a + b, a)
