import importlib

from utils.timeit import timeit


@timeit
def solve(problem_number: int):
    try:
        problem_module = importlib.import_module(f'problems.problem_{problem_number}')
        problem_class = getattr(problem_module, f"Problem{problem_number}")
    except:
        print(f'Problem {problem_number} is not solved yet!')
    else:
        problem = problem_class()
        title = problem.TITLE
        answer = problem.answer()
        print(f'The answer of problem {problem_number} ({title}) is {answer}.')


if __name__ == '__main__':
    solve(problem_number=22)
