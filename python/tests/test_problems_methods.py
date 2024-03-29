import pytest

from python.problems.problem_15 import Problem15
from python.problems.problem_21 import Problem21
from python.problems.problem_23 import Problem23
from python.problems.problem_26 import Problem26
from python.problems.problem_28 import Problem28
from python.problems.problem_37 import Problem37
from python.tests.test_case_problems_methods import (
    TEST_CASE_PROBLEM_21_D,
    TEST_CASE_PROBLEM_26_LENGTH_RECURRING_CYCLE,
)


@pytest.mark.parametrize("coordinates, expected_result", [([2, 2], 6)])
def test_problem_15_number_of_paths(coordinates, expected_result):
    assert (
        Problem15().number_of_paths(coordinates[0], coordinates[1]) == expected_result
    )


@pytest.mark.parametrize("number, expected_result", TEST_CASE_PROBLEM_21_D)
def test_problem_21_d(number, expected_result):
    assert Problem21().d(number=number) == expected_result


@pytest.mark.parametrize(
    "number, expected_result", [(5, False), (6, False), (12, True)]
)
def test_problem_23_is_abundant(number, expected_result):
    assert Problem23().is_abundant(number=number) == expected_result


@pytest.mark.parametrize(
    "fraction, expected_result", TEST_CASE_PROBLEM_26_LENGTH_RECURRING_CYCLE
)
def test_problem_26_length_recurring_cycle(fraction, expected_result):
    assert (
        Problem26().length_recurring_cycle(
            numerator=fraction[0], denominator=fraction[1]
        )
        == expected_result
    )


@pytest.mark.parametrize(
    "input, expected_result", [([3797, "left"], True), ([3797, "right"], True)]
)
def test_problem_37_is_a_truncable_prime(input, expected_result):
    assert (
        Problem37().is_a_truncable_prime(number=input[0], _from=input[1])
        == expected_result
    )


@pytest.mark.parametrize("length_side, expected_result", [(5, 101)])
def test_problem_28_diagonal_sequence(length_side, expected_result):
    assert (
        sum(Problem28().diagonal_sequence(length_side=length_side)) == expected_result
    )
