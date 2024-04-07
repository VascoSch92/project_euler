pub mod problem_4 {
    pub const TITLE: &str = "Largest palindrome product";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=4";

    pub fn answer() -> u32 {
        use std::cmp;
        use crate::utils::functions::functions_u32::is_palindrome;

        let mut answer: u32 = 0;
        for num_1 in (100..999).rev() {
            for num_2 in (100..999).rev() {
                if is_palindrome(num_1 * num_2) {
                    answer = cmp::max(answer, num_1 * num_2);
                }
            }
        }
        answer
    }

    pub fn pretty_print_solution() {
        use std::time::Instant;

        let now = Instant::now();
        let solution = answer();
        let elapsed = now.elapsed();

        println!("Problem {} - {}", 4, crate::problems::problem_4::problem_4::TITLE);
        println!("Description: {}", crate::problems::problem_4::problem_4::DESCRIPTION);
        println!("Solution: {}", solution);
        println!("Time: {:.2?}", elapsed);
    }

}