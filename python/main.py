import importlib
import sys
import time
from typing import Union, Tuple


def main() -> None:
    problem_number = catch_problem_number()
    solve(problem_number=problem_number)


def catch_problem_number() -> int:
    if len(sys.argv) == 0 or len(sys.argv) == 1:
        raise Exception("No command provided.")
    elif len(sys.argv) == 2:
        problem_number = sys.argv[1]
        try:
            problem_number = int(problem_number)
            return problem_number
        except ValueError:
            raise ValueError(
                f"Expected the problem's number to solve, but got {problem_number} instead."
            )
    else:
        raise ValueError(f"Expected 1 command, but got {len(sys.argv) -1}")


def solve(problem_number: int) -> None:
    try:
        problem_module = importlib.import_module(f"problems.problem_{problem_number}")
        problem_class = getattr(problem_module, f"Problem{problem_number}")
    except ImportError:
        print(f"Problem {problem_number} is not solved yet!")
    else:
        Problem = problem_class()
        execution_time, solution = _solve(problem=Problem)
        print(
            f"Problem {problem_number} - {Problem.TITLE} \n"
            f"Description: {Problem.DESCRIPTION} \n"
            f"Solution: {solution} \n"
            f"Time: {execution_time}ms"
        )


def _solve(problem) -> Tuple[float, Union[int, str]]:
    start_time = time.time()
    solution = problem.answer()
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    return execution_time, solution


if __name__ == "__main__":
    main()
