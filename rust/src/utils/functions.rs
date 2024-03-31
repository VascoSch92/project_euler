pub mod functions {

    pub fn number_of_divisors(n: &u32) -> u32 {
        let mut number_of_divisors: u32 = 0;

        for divisor in 1..=((*n as f64).sqrt() as u32) + 1 {
            if n % divisor == 0 {
                number_of_divisors += 1;

                if divisor != n / divisor {
                    number_of_divisors += 1;
                }
            }
        }
        number_of_divisors
    }

    pub fn triangular_number(n:u32) -> u32 {
        n * (n + 1) / 2
    }
}
