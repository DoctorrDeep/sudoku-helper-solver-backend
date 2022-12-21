"""Solve Sudoku using backtracking algorithm"""
import copy
import time

from src.helpers import ALL_XYS
from src.helpers.errors import SolverTimeoutError
from src.helpers.types import SudokuSquare
from src.settings import MAX_SOLUTIONS, TIMEOUT_FOR_RECURSION
from src.sudoku_cube import Sudoku


def check_insert(sudoku_square: SudokuSquare, x: int, y: int, val_to_insert: int) -> bool:
    """
    Check if inserting `val_to_insert` into position x row, y column
    is going to yield a valid sudoku block. Incomplete is valid too.
    """
    new_sudoku_square = copy.deepcopy(sudoku_square)
    new_sudoku_square[x][y] = val_to_insert
    return Sudoku.check_solution(new_sudoku_square)


def solve_square(sudoku: Sudoku, start_time: float = time.perf_counter(), timeout: float = TIMEOUT_FOR_RECURSION):
    """
    Backtracking algorithm where valid solutions are appended to
    the solutions property of Sudoku object.
    """
    now = time.perf_counter()
    if now - start_time > timeout:
        raise SolverTimeoutError(
            "Took more than %f to solve (%f s) using the backtracking method." % (timeout, now - start_time)
        )

    # Cycle through all cells in sudoku square
    for x, y in ALL_XYS:
        # If cell is empty then attempt fill in
        if not sudoku.sudoku_square_copy[x][y]:
            for i in sudoku.suggestions[(x, y)]:
                if len(sudoku.solutions) > MAX_SOLUTIONS:
                    return
                # If valid option found fill in the cell and
                # try arriving at a solution with the use of recursion
                if check_insert(sudoku.sudoku_square_copy, x, y, i):
                    sudoku.sudoku_square_copy[x][y] = i
                    solve_square(sudoku, start_time, timeout)
                    sudoku.sudoku_square_copy[x][y] = 0
            return

    if sudoku.sudoku_square_copy not in sudoku.solutions:
        sudoku.solutions.append(copy.deepcopy(sudoku.sudoku_square_copy))
