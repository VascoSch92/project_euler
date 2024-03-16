use std::time::Instant;

fn main() {

    let now = Instant::now();
    let solution = answer();
    let elapsed = now.elapsed();

    println!("The answer is {solution}");
    println!("Finding the answer took {:.2?}", elapsed);
}

fn answer() -> i32 {
    let mut sum_of_multiples: i32 = 0;
    for number in 1..1000 {
        if number % 3 == 0 || number % 5 == 0 {
            sum_of_multiples += number;
        }
    }
    sum_of_multiples
}