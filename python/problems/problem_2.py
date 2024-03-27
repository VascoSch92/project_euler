class Problem2:
    TITLE = "Even Fibonacci number"
    DESCRIPTION = "https://projecteuler.net/problem=2"

    def answer(self) -> int:
        sum_even_valued_terms = 0

        fib_n_1, fib_n = 1, 2
        new_fib = 2

        while fib_n < 4_000_000:
            if new_fib % 2 == 0:
                sum_even_valued_terms += new_fib

            new_fib = fib_n_1 + fib_n
            fib_n_1, fib_n = fib_n, new_fib

        return sum_even_valued_terms
