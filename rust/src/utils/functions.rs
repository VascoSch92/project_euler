pub mod functions {

    pub fn is_prime(n: u32) -> bool {
        if n <= 3 {
            return true;
        };
        if n % 2 == 0 || n % 3 == 0 {
            return false;
        };
        for divisor in (5..=((n as f64).sqrt() as u32) + 1).step_by(2){
            if n % divisor == 0 || n % (divisor + 2) == 0 {
                return false;
            }
        };
        return true;
    }

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
