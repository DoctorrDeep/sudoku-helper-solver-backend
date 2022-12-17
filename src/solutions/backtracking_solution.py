"""Solve Sudoku using backtracking algorithm"""
import copy
from pprint import pprint

from src.helpers import ALL_XYS
from src.helpers.types import SudokuSquare
from src.helpers.verifiers import check_solution
from src.sudoku_cube import Sudoku

LAST_KNOWN_GOOD_SOLUTION = []


def check_insert(sudoku_square: SudokuSquare, x: int, y: int, val_to_insert: int) -> bool:
    """
    Check if inserting `val_to_insert` into position x row, y column
    is going to yield a valid sudoku block. Incomplete is valid too.
    """
    new_sudoku_square = copy.deepcopy(sudoku_square)
    new_sudoku_square[x][y] = val_to_insert
    return check_solution(new_sudoku_square)


def solve(sudoku_square: SudokuSquare, verbose: bool | None = False):
    """
    Backtracking algorithm where valid solutions are updated to
    the `LAST_KNOWN_GOOD_SOLUTION` variable. There might be multiple
    correct answers to the sudoku, hence "last_known_..."
    """

    # Cycle through all cells in sudoku square
    for x, y in ALL_XYS:
        # If cell is empty then attempt fill in
        if not sudoku_square[x][y]:
            for i in range(1, 10):
                # If valid option found fill in the cell and
                # try arriving at a solution with the use of recursion
                if check_insert(sudoku_square, x, y, i):
                    sudoku_square[x][y] = i
                    solve(sudoku_square, verbose)
                    sudoku_square[x][y] = 0
            return

    if verbose:
        print("Found Solution:")
        pprint(sudoku_square)

    global LAST_KNOWN_GOOD_SOLUTION
    LAST_KNOWN_GOOD_SOLUTION = copy.deepcopy(sudoku_square)


def solve_square(sudoku: Sudoku):
    """
    Backtracking algorithm where valid solutions are appended to
    the solutions property of Sudoku object.
    """
    # Cycle through all cells in sudoku square
    for x, y in ALL_XYS:
        # If cell is empty then attempt fill in
        if not sudoku.sudoku_square_copy[x][y]:
            for i in sudoku.suggestions[(x, y)]:
                if len(sudoku.solutions) > 5:
                    return
                # If valid option found fill in the cell and
                # try arriving at a solution with the use of recursion
                if check_insert(sudoku.sudoku_square_copy, x, y, i):
                    sudoku.sudoku_square_copy[x][y] = i
                    solve_square(sudoku)
                    sudoku.sudoku_square_copy[x][y] = 0
            return

    if sudoku.sudoku_square_copy not in sudoku.solutions:
        sudoku.solutions.append(copy.deepcopy(sudoku.sudoku_square_copy))


def solve_and_return_result(sudoku_square: SudokuSquare) -> SudokuSquare:
    """
    Solve and return the completed sudoku.
    Note: final return statement in solve() did not work. Any idea why?
    """
    solve(sudoku_square)
    return LAST_KNOWN_GOOD_SOLUTION
