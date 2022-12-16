from src.example_problems import EASY_SUDOKU, SOLVED_SUDOKU
from src.solutions import backtracking_solution


def test_easy_backtracking_solution():
    assert SOLVED_SUDOKU == backtracking_solution.solve_and_return_result(EASY_SUDOKU)
