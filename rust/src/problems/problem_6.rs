pub mod problem_6 {
    pub const TITLE: &str = "Sum square difference";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=6";

    pub fn answer() -> i32 {
        let mut sum_of_the_squares: i32 = 0;
        let mut sum: i32 = 0;

        for number in 1..=100 {
            sum_of_the_squares += (number as i32).pow(2);
            sum += number;
        }
        sum.pow(2) - sum_of_the_squares
    }

    pub fn pretty_print_solution() {
        use std::time::Instant;

        let now = Instant::now();
        let solution = answer();
        let elapsed = now.elapsed();

        println!("Problem {} - {}", 6, crate::problems::problem_6::problem_6::TITLE);
        println!("Description: {}", crate::problems::problem_6::problem_6::DESCRIPTION);
        println!("Solution: {}", solution);
        println!("Time: {:.2?}", elapsed);
    }
}