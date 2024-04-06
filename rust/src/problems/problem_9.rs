pub mod problem_9 {
    pub const TITLE: &str = "Special Pythagoren triplet";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=9";

    pub fn answer() -> i32 {
        for a in 0..999 {
            for b in a+1..1000 {
                let a = a as f32;
                let b = b as f32;
                let c: f32 = (a.powi(2) + b.powi(2)).sqrt();

                if b < c && a + b + c == 1000. {
                    return (a*b*c) as i32;
                }
            }
        }
        panic!("No solution found!")
    }

    pub fn pretty_print_solution() {
        use std::time::Instant;

        let now = Instant::now();
        let solution = answer();
        let elapsed = now.elapsed();

        println!("Problem {} - {}", 9, crate::problems::problem_9::problem_9::TITLE);
        println!("Description: {}", crate::problems::problem_9::problem_9::DESCRIPTION);
        println!("Solution: {}", solution);
        println!("Time: {:.2?}", elapsed);
    }
}