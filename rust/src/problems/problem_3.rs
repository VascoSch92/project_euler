pub mod problem_3 {
    pub const TITLE: &str = "Largest prime factor";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=3";

    pub fn answer() -> u64 {
        use crate::utils::functions::functions_u64::is_prime;

        let mut number: u64 = 600_851_475_143;
        let mut divisor: u64 = 2;

        while is_prime(number) == false {
            if number % divisor == 0 {
                number /= divisor;
            } else if divisor == number - 1{
                return number;
            } else {
                divisor += 1;
            }
        }
        number
    }

    pub fn pretty_print_solution() {
        use std::time::Instant;

        let now = Instant::now();
        let solution = answer();
        let elapsed = now.elapsed();

        println!("Problem {} - {}", 3, crate::problems::problem_3::problem_3::TITLE);
        println!("Description: {}", crate::problems::problem_3::problem_3::DESCRIPTION);
        println!("Solution: {}", solution);
        println!("Time: {:.2?}", elapsed);
    }

}