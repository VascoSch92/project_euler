class Problem25:
    TITLE = '1000-digit Fibonacci number'
    DESCRIPTION = 'https://projecteuler.net/problem=25'

    def answer(self) -> int:
        fib_n_1, fib_n = 1, 1
        index = 2

        while not self.has_1000_digits(fib_n):
            new_fib = fib_n_1 + fib_n
            fib_n_1, fib_n = fib_n, new_fib
            index += 1

        return index

    @staticmethod
    def has_1000_digits(number: int) -> bool:
        return len(str(number)) == 1_000
