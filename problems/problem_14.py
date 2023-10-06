class Problem14:
    TITLE = 'Longest Collatz sequence'
    DESCRIPTION = 'https://projecteuler.net/problem=14'

    map_starting_number_and_length = {}

    def answer(self) -> int:
        starting_number_with_max_length = float('-inf')
        max_length = float('-inf')

        for starting_number in range(2, 1_000_000):
            starting_number_length = self.length_collatz_sequence(starting_number=starting_number)
            if starting_number_length > max_length:
                starting_number_with_max_length = starting_number
                max_length = starting_number_length

        return starting_number_with_max_length

    def length_collatz_sequence(self, starting_number: int) -> int:
        length = 0
        number = starting_number

        while number != 1:
            length += 1
            if number in self.map_starting_number_and_length.keys():
                length += self.map_starting_number_and_length[number]
                break

            if number % 2 == 0:
                number = number / 2
            else:
                number = 3 * number + 1

        self.map_starting_number_and_length[starting_number] = length
        return length
