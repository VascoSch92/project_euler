pub mod problem_836 {
    pub const TITLE: &str = "A Bold Proposition";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=836";

    pub fn answer() -> String {
        "aprilfoolsjoke".to_string()
    }

    pub fn pretty_print_solution() {
        use std::time::Instant;

        let now = Instant::now();
        let solution = answer();
        let elapsed = now.elapsed();

        println!("Problem {} - {}", 836, crate::problems::problem_836::problem_836::TITLE);
        println!("Description: {}", crate::problems::problem_836::problem_836::DESCRIPTION);
        println!("Solution: {}", solution);
        println!("Time: {:.2?}", elapsed);
    }
}