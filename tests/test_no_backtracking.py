import pytest

from src.example_problems import EASY_SUDOKU, SOLVED_SUDOKU
from src.solutions.no_backtracking_solution import try_fill_in
from src.sudoku_cube import Sudoku

SUDOKU = Sudoku(EASY_SUDOKU)
SUDOKU.run_solver(try_fill_in)

test_solution_and_length_of_suggestions = [
    (SUDOKU.solutions[0], SOLVED_SUDOKU),
    (len(SUDOKU.suggestions.keys()), 0),
]


@pytest.mark.parametrize("test_data,expected", test_solution_and_length_of_suggestions)
def test_easy_backtracking_solution(test_data, expected):
    assert test_data == expected
