from utils.functions import is_prime


class Problem27:
    TITLE = 'Quadratic primes'
    DESCRIPTION = 'https://projecteuler.net/problem=27'

    def answer(self) -> int:
        product_coeff, max_number_of_primes = float('-inf'), float('-inf')

        for a in range(-999, 1000):
            for b in range(a ** 2 // 4, 1000):
                n = 0
                while is_prime(n ** 2 + a * n + b):
                    n += 1

                if n > max_number_of_primes:
                    max_number_of_primes = n
                    product_coeff = a * b

        return product_coeff
