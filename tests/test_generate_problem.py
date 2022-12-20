from src.helpers.generate_problems import create_sudoku_problem
from src.helpers.types import Level

EASY_SUDOKU = create_sudoku_problem(level=Level.easy)
DIFFICULT_SUDOKU = create_sudoku_problem(level=Level.difficult)


def test_make_easy_problem():
    assert EASY_SUDOKU.get_max_suggestions_count() == 2


def test_make_difficult_problem():
    assert DIFFICULT_SUDOKU.get_max_suggestions_count() == 3
