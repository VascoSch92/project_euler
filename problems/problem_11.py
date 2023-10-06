import numpy as np


class Problem11:
    TITLE = 'Largest product in a grid'
    DESCRIPTION = 'https://projecteuler.net/problem=11'

    def answer(self) -> int:
        grid = self.read_grid_from_txt(path='files/problem_11.txt')

        max_prod = float('-inf')
        for idx_row in range(0, 16):
            for idx_col in range(0, 16):
                subarray = grid[idx_row:idx_row + 4, idx_col: idx_col + 4]
                prod = self.compute_max_prod_in_subarray(subarray=subarray)
                max_prod = max(prod, max_prod)
        return max_prod

    @staticmethod
    def read_grid_from_txt(path: str) -> np.ndarray:
        with open(path) as file_txt:
            grid = []
            for line in file_txt.readlines():
                line = line.strip().split(' ')
                grid.append([int(number) for number in line])

            return np.array(grid)

    @staticmethod
    def compute_max_prod_in_subarray(subarray: np.ndarray) -> int:
        return np.max([
            np.prod(subarray[0, :]),  # horizontal
            np.prod(subarray[:, 0]),  # vertical
            np.prod(subarray.diagonal()),  # diagonal from right to left
            np.prod(np.fliplr(subarray).diagonal()),  # diagonal from left to right
        ]
        )
