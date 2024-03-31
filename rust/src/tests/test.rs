#[cfg(test)]
pub mod tests {
    use rstest::rstest;
    use crate::utils::functions::functions::number_of_divisors;
    use crate::utils::functions::functions::triangular_number;
    use crate::utils::functions::functions::is_prime;

    #[rstest]
    #[case(2, true)]
    #[case(3, true)]
    #[case(7, true)]
    #[case(10, false)]
    fn test_is_prime(#[case] input: u32, #[case] expected: bool) {
        assert_eq!(expected, is_prime(input));
    }

    #[rstest]
    #[case(1, 1)]
    #[case(8, 4)]
    #[case(100, 9)]
    fn test_number_of_divisors(#[case] input: u32, #[case] expected: u32) {
        assert_eq!(expected, number_of_divisors(&input));
    }

    #[rstest]
    #[case(0, 0)]
    #[case(1, 1)]
    #[case(8, 36)]
    #[case(36, 666)]
    fn test_triangular_number(#[case] input: u32, #[case] expected: u32) {
        assert_eq!(expected, triangular_number(input));
    }


}