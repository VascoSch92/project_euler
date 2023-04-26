import pytest
from problems.problem_21 import Problem21

from tests.test_case_problems_methods import TEST_CASE_D


@pytest.mark.parametrize("number, expected_result", TEST_CASE_D)
def test_d(number, expected_result):
    assert Problem21().d(number=number) == expected_result
