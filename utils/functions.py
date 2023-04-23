from math import sqrt

def is_palindrome(number: int) -> bool:
    """ The method return True if the input number is palindrome. Otherwise, False """
    return str(number) == str(number)[::-1]

def is_prime(number: int) -> bool:
    """ The method return True if the input number is prime. Otherwise, False """
    assert number > 0, f'The input number {number} is not positive'

    if number in [0, 1]:
        return False
    elif number == 2:
        return True
    else:
        for d in range(3, int(sqrt(number))+1, 2):
            if number%d==0:
                return False

        return True

