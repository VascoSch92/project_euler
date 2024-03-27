pub mod problem_2 {
    pub const TITLE: &str = "Even Fibonacci number";
    pub const DESCRIPTION: &str = "https://projecteuler.net/problem=2";

    pub fn answer() -> i32 {
        let mut sum_even_valued_terms: i32 = 0;

        let mut fib_n_1: i32 = 1;
        let mut fib_n: i32 = 2;
        let mut new_fib: i32 = 2;

        while fib_n < 4000000 {
            if new_fib % 2 == 0 {
                sum_even_valued_terms += new_fib;
            }

            new_fib = fib_n_1 + fib_n;
            fib_n_1 = fib_n;
            fib_n = new_fib;
        }
        sum_even_valued_terms
    }
}
