pub mod problem_63{
    pub const TITLE: &str = "";
    pub const DESCRIPTION: &str = "";

    pub fn answer() -> u64 {
        let mut count: u64 = 0;

        for base in 1..=10 {
            for power in 1..=23 {
                let length_of_power: u64 = ((base as u64).pow(power as u32)).to_string().len().try_into().unwrap();

                if length_of_power == power {
                    count += 1
                };
            }
        }
        count
    }

    pub fn pretty_print_solution() {
        use std::time::Instant;

        let now = Instant::now();
        let solution = answer();
        let elapsed = now.elapsed();

        println!("Problem {} - {}", 63, crate::problems::problem_63::problem_63::TITLE);
        println!("Description: {}", crate::problems::problem_63::problem_63::DESCRIPTION);
        println!("Solution: {}", solution);
        println!("Time: {:.2?}", elapsed);
    }
}