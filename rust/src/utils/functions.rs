pub mod functions_u32 {

    pub fn is_pentagonal(number: &u32) -> bool {
        let n: f32 = *number as f32;
        let index: f32 = (1. + (1. + 24. * n).sqrt()) / 6.;
        if index == index.floor() {
            true
        } else {
            false
        }
    }

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
        true
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

    pub fn pentagonal_number(n:u32) -> u32 {
        n * (3*n -1) / 2
    }

    pub fn triangular_number(n:u32) -> u32 {
        n * (n + 1) / 2
    }
}

pub mod functions_u64 {

    pub fn is_prime(n: u64) -> bool {
        if n <= 3 {
            return true;
        };
        if n % 2 == 0 || n % 3 == 0 {
            return false;
        };
        for divisor in (5..=((n as f64).sqrt() as u64) + 1).step_by(2){
            if n % divisor == 0 || n % (divisor + 2) == 0 {
                return false;
            }
        };
        true
    }

}