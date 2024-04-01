pub mod problem_12 {
    pub const TITLE: &str = "Highly divisible triangular number";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=12";

    pub fn answer() -> u32 {
        use crate::utils::functions::functions_u32::number_of_divisors;
        use crate::utils::functions::functions_u32::triangular_number;

        let mut n: u32 = 500;
        let mut t_n: u32 = triangular_number(n);

        while number_of_divisors(&t_n) < 500 {
            n += 1;
            t_n = triangular_number(n);
        }
        t_n
    }

    pub fn pretty_print_solution() {
        use std::time::Instant;

        let now = Instant::now();
        let solution = answer();
        let elapsed = now.elapsed();

        println!("Problem {} - {}", 12, crate::problems::problem_12::problem_12::TITLE);
        println!("Description: {}", crate::problems::problem_12::problem_12::DESCRIPTION);
        println!("Solution: {}", solution);
        println!("Time: {:.2?}", elapsed);
    }
}