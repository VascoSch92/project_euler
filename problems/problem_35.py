from utils.functions import is_prime


class Problem35:
    TITLE = 'Circular primes'
    DESCRIPTION = 'https://projecteuler.net/problem=35'

    def answer(self) -> int:
        count = 0
        for number in range(2, 1_000_000):
            if is_prime(number=number):
                if self.is_circular_prime(number=number):
                    count += 1

        return count

    @staticmethod
    def is_circular_prime(number: int) -> bool:
        number = str(number)
        permutations = {number[x:] + number[:x] for x in range(len(number))}

        for perm in permutations:
            if not is_prime(int(perm)):
                return False
        return True
