from collections import defaultdict


class Problem62:
    TITLE = 'Cubic Permutations'
    DESCRIPTION = 'https://projecteuler.net/problem=62'

    def answer(self) -> int:
        side = 1
        cube_dict = defaultdict(lambda: [0, []])

        while True:
            cube = str(side ** 3)
            sorted_cube = ''.join(sorted(cube))
            cube_dict[sorted_cube][0] += 1
            cube_dict[sorted_cube][1].append(cube)

            if cube_dict[sorted_cube][0] == 5:
                return int(cube_dict[sorted_cube][1][0])
            else:
                side += 1
