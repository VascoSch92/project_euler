pub mod problem_10 {
    pub const TITLE: &str = "Summation of primes";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=10";

    fn answer() -> u64 {
        use crate::utils::functions::functions_u64::is_prime;

        let mut summation_of_primes: u64 = 2;

        for number in (3..2000000).step_by(2) {
            if is_prime(number) {
                summation_of_primes += number;
            }
        }
        summation_of_primes
    }

    pub fn pretty_print_solution() {
        use std::time::Instant;

        let now = Instant::now();
        let solution = answer();
        let elapsed = now.elapsed();

        println!("Problem {} - {}", 10, crate::problems::problem_10::problem_10::TITLE);
        println!("Description: {}", crate::problems::problem_10::problem_10::DESCRIPTION);
        println!("Solution: {}", solution);
        println!("Time: {:.2?}", elapsed);
    }
}