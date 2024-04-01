pub mod problem_7 {
    pub const TITLE: &str = "10001st prime";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=7";

    pub fn answer() -> u32 {
        use crate::utils::functions::functions_u32::is_prime;

        let mut prime_numbers_count: u32 = 0;
        let mut number: u32 = 0;

        while prime_numbers_count <= 10000 {
            number += 1;

            if is_prime(number) {
                prime_numbers_count += 1;
            }
        }
        number
    }

    pub fn pretty_print_solution() {
        use std::time::Instant;

        let now = Instant::now();
        let solution = answer();
        let elapsed = now.elapsed();

        println!("Problem {} - {}", 7, crate::problems::problem_7::problem_7::TITLE);
        println!("Description: {}", crate::problems::problem_7::problem_7::DESCRIPTION);
        println!("Solution: {}", solution);
        println!("Time: {:.2?}", elapsed);
    }

}