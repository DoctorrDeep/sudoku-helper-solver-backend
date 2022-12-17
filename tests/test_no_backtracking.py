from src.example_problems import EASY_SUDOKU, SOLVED_SUDOKU
from src.solutions import no_backtracking_solution


def test_easy_no_backtracking_solution():
    assert no_backtracking_solution.try_fill_in(EASY_SUDOKU) == SOLVED_SUDOKU
