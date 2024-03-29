import pytest

from python.tests.test_cases_for_functions import (
    TEST_CASE_IS_PRIME,
    TEST_CASE_IS_PALINDROME,
    TEST_CASE_TRIANGULAR_NUMBER,
    TEST_CASE_NUMBER_OF_DIVISORS,
    TEST_CASE_IS_A_TRIANGULAR_NUMBER,
    TEST_CASE_SUM_OF_DIGITS,
    TEST_CASE_EULER_TOTIENT_FUNCTION,
    TEST_CASE_MAX_PATH_SUM_TRIANGLE,
)
from python.utils.functions import (
    is_palindrome,
    is_prime,
    is_a_triangular_number,
    triangular_number,
    number_of_divisors,
    sum_of_digits,
    euler_totient_function,
    max_path_sum_triangle,
)


@pytest.mark.parametrize("number, expected_result", TEST_CASE_EULER_TOTIENT_FUNCTION)
def test_euler_totient_function(number, expected_result):
    assert euler_totient_function(number) == expected_result


@pytest.mark.parametrize("number, expected_result", TEST_CASE_IS_PALINDROME)
def test_is_palindrome(number, expected_result):
    assert is_palindrome(number) == expected_result


@pytest.mark.parametrize("number, expected_result", TEST_CASE_IS_PRIME)
def test_is_prime(number, expected_result):
    assert is_prime(number) == expected_result


@pytest.mark.parametrize("number, expected_result", TEST_CASE_IS_A_TRIANGULAR_NUMBER)
def test_is_a_triangular_number(number, expected_result):
    assert is_a_triangular_number(number) == expected_result


@pytest.mark.parametrize("triangle, expected_result", TEST_CASE_MAX_PATH_SUM_TRIANGLE)
def test_max_sum_path_triangle(triangle, expected_result):
    assert max_path_sum_triangle(triangle) == expected_result


@pytest.mark.parametrize("number, expected_result", TEST_CASE_SUM_OF_DIGITS)
def test_sum_of_digits(number, expected_result):
    assert sum_of_digits(number) == expected_result


@pytest.mark.parametrize("number, expected_result", TEST_CASE_NUMBER_OF_DIVISORS)
def test_number_of_divisors(number, expected_result):
    assert number_of_divisors(number) == expected_result


@pytest.mark.parametrize("number, expected_result", TEST_CASE_TRIANGULAR_NUMBER)
def test_triangular_number(number, expected_result):
    assert triangular_number(number) == expected_result
