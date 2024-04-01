use std::env;

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
        1 => problems::problem_1::problem_1::pretty_print_solution(),
        2 => problems::problem_2::problem_2::pretty_print_solution(),
        3 => problems::problem_3::problem_3::pretty_print_solution(),
        5 => problems::problem_5::problem_5::pretty_print_solution(),
        6 => problems::problem_6::problem_6::pretty_print_solution(),
        7 => problems::problem_7::problem_7::pretty_print_solution(),
        10 => problems::problem_10::problem_10::pretty_print_solution(),
        12 => problems::problem_12::problem_12::pretty_print_solution(),
        _ => panic!("Problem {} is not solved yet", problem_number),
    };
}
