import pytest

from src.example_problems import EASY_SUDOKU
from src.helpers.verifiers import do_check
from src.sudoku_cube import Sudoku

test_data = [
    (range(1, 10), True),
    (range(2, 11), False),
    (range(9), True),
    ([0, 1, 2, 0, 4, 0, 6, 7, 8], True),
    ([1, 9, 2, 1, 4, 1, 6, 7, 1], False),
]

DUMMY_SQUARE = Sudoku(EASY_SUDOKU)


@pytest.mark.parametrize("check_input,expected", test_data)
def test_old_do_check(check_input, expected):
    assert do_check(check_input) == expected


@pytest.mark.parametrize("check_input,expected", test_data)
def test_do_check(check_input, expected):
    assert Sudoku.check(check_input) == expected


@pytest.mark.parametrize("check_input,expected", test_data)
def test_do_strict_check(check_input, expected):
    modified_expected = expected if 0 not in check_input else False
    assert DUMMY_SQUARE.strict_check(check_input) == modified_expected
