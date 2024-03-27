from python.utils.functions import is_prime


class Problem37:
    TITLE = "Truncatable primes"
    DESCRIPTION = "https://projecteuler.net/problem=37"

    def answer(self) -> int:
        sum_of_truncable_primes = 0
        number = 21
        count = 0

        while count < 11:
            string_number = str(number)
            if string_number.endswith("5") or string_number.endswith("9"):
                number += 2
                continue
            if "0" in string_number or "4" in string_number or "8" in string_number:
                number += 2
                continue
            if self.is_a_truncable_prime(number=number, _from="left"):
                if self.is_a_truncable_prime(number=number, _from="right"):
                    sum_of_truncable_primes += number
                    count += 1
            number += 2

        return sum_of_truncable_primes

    def is_a_truncable_prime(self, number: int, _from: str) -> bool:
        assert _from in [
            "left",
            "right",
        ], f"The variable _from must be left or right, but is {_from}."

        if _from == "left":
            while number > 0:
                if is_prime(number=number):
                    if number > 10:
                        number = int(str(number)[1:])
                    else:
                        number = 0
                else:
                    return False
        else:
            while number > 0:
                if is_prime(number=number):
                    number //= 10
                else:
                    return False
        return True
