from utils.functions import is_prime


class Problem35:
    TITLE = 'Circular primes'
    DESCRIPTION = "The number, 197, is called a circular prime because all rotations of the ndigits: 197, 971,\n" \
                  " and 719, are themselves prime. There are thirteen such primes below 100: 2, 3, 5, 7, 11,\n" \
                  " 13, 17, 31, 37, 71, 73, 79, and 97. How many circular primes are there below one million?"

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
