pub mod problem_1 {
    pub const TITLE: &str = "Multiples of 3 or 5";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=1";

    pub fn answer() -> i32 {
        let mut sum_of_multiples: i32 = 0;
        for number in 1..1000 {
            if number % 3 == 0 || number % 5 == 0 {
                sum_of_multiples += number;
            }
        }
        sum_of_multiples
    }
}