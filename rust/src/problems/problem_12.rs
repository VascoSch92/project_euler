pub mod problem_12 {
    use crate::utils::functions::functions::number_of_divisors;
    use crate::utils::functions::functions::triangular_number;

    pub const TITLE: &str = "Highly divisible triangular number";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=12";

    pub fn answer() -> u32 {
        let mut n: u32 = 500;
        let mut t_n: u32 = triangular_number(n);

        while number_of_divisors(&t_n) < 500 {
            n += 1;
            t_n = triangular_number(n);
        }
        t_n
    }
}