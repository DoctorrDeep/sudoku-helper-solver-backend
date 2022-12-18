"""Solve Sudoku using backtracking algorithm"""
import copy

from src.helpers import ALL_XYS
from src.helpers.types import SudokuSquare
from src.helpers.verifiers import check_solution
from src.sudoku_cube import Sudoku


def check_insert(sudoku_square: SudokuSquare, x: int, y: int, val_to_insert: int) -> bool:
    """
    Check if inserting `val_to_insert` into position x row, y column
    is going to yield a valid sudoku block. Incomplete is valid too.
    """
    new_sudoku_square = copy.deepcopy(sudoku_square)
    new_sudoku_square[x][y] = val_to_insert
    return check_solution(new_sudoku_square)


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
