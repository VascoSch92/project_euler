pub mod problem_44 {
    pub const TITLE: &str = "Pentagon numbers";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=44";

    pub fn answer() -> u32 {
        use crate::utils::functions::functions_u32::pentagonal_number;
        use crate::utils::functions::functions_u32::is_pentagonal;

        let mut idx_1: u32 = 2;

        loop {
            for idx_2 in 1..idx_1 {
                let p_1 = pentagonal_number(idx_1);
                let p_2 = pentagonal_number(idx_2);

                if is_pentagonal(&(p_1 - p_2)) && is_pentagonal(&(p_1 + p_2)){
                    return p_1 - p_2;
                };
            }
            idx_1 += 1
        }
    }

    pub fn pretty_print_solution() {
        use std::time::Instant;

        let now = Instant::now();
        let solution = answer();
        let elapsed = now.elapsed();

        println!("Problem {} - {}", 44, crate::problems::problem_44::problem_44::TITLE);
        println!("Description: {}", crate::problems::problem_44::problem_44::DESCRIPTION);
        println!("Solution: {}", solution);
        println!("Time: {:.2?}", elapsed);
    }
}