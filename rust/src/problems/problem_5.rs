pub mod problem_5 {
    pub const TITLE: &str = "Smallest multiple";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=5";

    pub fn answer() -> i32 {
        1 * 2_i32.pow(4) * 3_i32.pow(2) * 5 * 7 * 11 * 13 * 17 * 19
    }
}