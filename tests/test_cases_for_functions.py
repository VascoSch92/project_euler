TEST_CASE_IS_PALINDROME = [
    (-1, False),
    (0, True),
    (11, True),
    (12, False),
    (123, False),
    (121, True),
]

TEST_CASE_IS_PRIME = [
    (-1, False),
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (11, True),
]

TEST_CASE_IS_A_TRIANGULAR_NUMBER = [
    (1, True),
    (2, False),
    (3, True),
    (4, False),
    (5, False),
    (6, True),
    (28, True),
]

TEST_CASE_SUM_OF_DIGITS = [
    (1, 1),
    (10, 1),
    (222, 6),
    (3_628_800, 27),
]

TEST_CASE_TRIANGULAR_NUMBER = [
    (1, 1),
    (2, 3),
    (3, 6),
    (4, 10),
    (5, 15),
    (6, 21),
    (7, 28),
]

TEST_CASE_NUMBER_OF_DIVISORS = [
    (1, 1),
    (3, 2),
    (6, 4),
    (10, 4),
    (28, 6),
]
