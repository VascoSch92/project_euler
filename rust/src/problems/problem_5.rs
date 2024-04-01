pub mod problem_5 {
    pub const TITLE: &str = "Smallest multiple";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=5";

    pub fn answer() -> i32 {
        2_i32.pow(4) * 3_i32.pow(2) * 5 * 7 * 11 * 13 * 17 * 19
    }

    pub fn pretty_print_solution() {
        use std::time::Instant;

        let now = Instant::now();
        let solution = answer();
        let elapsed = now.elapsed();

        println!("Problem {} - {}", 5, crate::problems::problem_5::problem_5::TITLE);
        println!("Description: {}", crate::problems::problem_5::problem_5::DESCRIPTION);
        println!("Solution: {}", solution);
        println!("Time: {:.2?}", elapsed);
    }
}