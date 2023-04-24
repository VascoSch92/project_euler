import pytest

from tests.test_cases_for_functions import TEST_CASE_IS_PRIME, TEST_CASE_IS_PALINDROME
from utils.functions import is_palindrome, is_prime


@pytest.mark.parametrize("number, expected_result", TEST_CASE_IS_PALINDROME)
def test_is_palindrome(number, expected_result):
    assert is_palindrome(number) == expected_result


@pytest.mark.parametrize("number, expected_result", TEST_CASE_IS_PRIME)
def test_is_prime(number, expected_result):
    assert is_prime(number) == expected_result
