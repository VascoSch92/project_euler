use std::env;
use std::time::Instant;
use std::time::Duration;

mod problems;
mod tests;
mod utils;

fn main() {
    let command: String = get_command();
    let problem_number: u32 = validate_command(command);
    solve_problem(problem_number);
}

fn get_command() -> String {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        1 => panic!("No command provided."),
        2 => (*args[1]).to_string(),
        _ => panic!("Expected 1 command but got {}", args.len() - 1),
    }
}

fn validate_command(command: String) -> u32 {
    match command.parse() {
        Ok(number) => number,
        Err(error) => panic!("{}", error),
    }
}

fn solve_problem(problem_number: u32){
    match problem_number {
        0 => panic!("There is no problem 0 in project Euler."),
        1 => {
            let now = Instant::now();
            let solution = problems::problem_1::problem_1::answer();
            let elapsed = now.elapsed();

            pretty_print_solution(
                problems::problem_1::problem_1::TITLE,
                problems::problem_1::problem_1::DESCRIPTION,
                problem_number,
                solution,
                elapsed,
            );
        },
        2 => {
            let now = Instant::now();
            let solution = problems::problem_2::problem_2::answer();
            let elapsed = now.elapsed();

            pretty_print_solution(
                problems::problem_2::problem_2::TITLE,
                problems::problem_2::problem_2::DESCRIPTION,
                problem_number,
                solution,
                elapsed,
            );
        },
        5 => {
            let now = Instant::now();
            let solution = problems::problem_5::problem_5::answer();
            let elapsed = now.elapsed();

            pretty_print_solution(
                problems::problem_5::problem_5::TITLE,
                problems::problem_5::problem_5::DESCRIPTION,
                problem_number,
                solution,
                elapsed,
            );
        },
        6 => {
            let now = Instant::now();
            let solution = problems::problem_6::problem_6::answer();
            let elapsed = now.elapsed();

            pretty_print_solution(
                problems::problem_6::problem_6::TITLE,
                problems::problem_6::problem_6::DESCRIPTION,
                problem_number,
                solution,
                elapsed,
            );
        },
        12 => {
            let now = Instant::now();
            let solution = problems::problem_12::problem_12::answer();
            let elapsed = now.elapsed();

            pretty_print_solution(
                problems::problem_12::problem_12::TITLE,
                problems::problem_12::problem_12::DESCRIPTION,
                problem_number,
                solution as i32,
                elapsed,
            );
        },
        _ => panic!("Problem {} is not solved yet", problem_number),
    };
}

fn pretty_print_solution(title: &str, description: &str, problem_number: u32, solution: i32, time: Duration) {
    println!("Problem {} - {}", problem_number, title);
    println!("Description: {}", description);
    println!("Solution: {}", solution);
    println!("Time: {:.2?}", time);
}
