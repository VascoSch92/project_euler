import pytest
from problems.problem_15 import Problem15
from problems.problem_21 import Problem21
from problems.problem_23 import Problem23
from problems.problem_28 import Problem28
from problems.problem_820 import Problem820

from tests.test_case_problems_methods import TEST_CASE_PROBLEM_21_D, TEST_CASE_PROBLEM_820_D, TEST_CASE_PROBLEM_820_S


@pytest.mark.parametrize("coordinates, expected_result", [([2, 2], 6)])
def test_problem_15_number_of_paths(coordinates, expected_result):
    assert Problem15().number_of_paths(coordinates[0], coordinates[1]) == expected_result


@pytest.mark.parametrize("number, expected_result", TEST_CASE_PROBLEM_21_D)
def test_problem_21_d(number, expected_result):
    assert Problem21().d(number=number) == expected_result


@pytest.mark.parametrize("number, expected_result", [(5, False), (6, False), (12, True)])
def test_problem_23_is_abundant(number, expected_result):
    assert Problem23().is_abundant(number=number) == expected_result


@pytest.mark.parametrize("length_side, expected_result", [(5, 101)])
def test_problem_28_diagonal_sequence(length_side, expected_result):
    assert sum(Problem28().diagonal_sequence(length_side=length_side)) == expected_result


@pytest.mark.parametrize("input, expected_result", TEST_CASE_PROBLEM_820_D)
def test_problem_820_d(input, expected_result):
    assert Problem820().d(n=input[0], x=input[1]) == expected_result


@pytest.mark.parametrize("n, expected_result", TEST_CASE_PROBLEM_820_S)
def test_problem_820_s(n, expected_result):
    assert Problem820().s(n=n) == expected_result
