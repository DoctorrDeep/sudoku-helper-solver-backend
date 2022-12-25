"""Solve Sudoku using recursion only"""
import copy
import time

from src.helpers.errors import SolverTimeoutError
from src.settings import TIMEOUT_FOR_RECURSION
from src.sudoku_cube import Sudoku


def try_fill_in(sudoku: Sudoku, start_time: float):
    """
    Attempts will be made to fill in given sudoku square where only 1 suggestion is to be had
    """

    now = time.perf_counter()
    if now - start_time > TIMEOUT_FOR_RECURSION:
        raise SolverTimeoutError(
            "Took more than %i to solve (%f s) using the no-backtracking method."
            % (TIMEOUT_FOR_RECURSION, now - start_time)
        )

    found_a_solution = False
    used_suggestions_count = 0
    suggestions = Sudoku.get_suggestions(sudoku.sudoku_square_copy)  # Calculate suggestions in latest state

    # Update sudoku square with found solutions
    for xy, cell_values in suggestions.items():
        if len(cell_values) == 1:
            found_a_solution = True
            used_suggestions_count += 1
            sudoku.sudoku_square_copy[xy[0]][xy[1]] = cell_values[0]

    if found_a_solution:
        # If all suggestions have been used up, then return from solver
        if used_suggestions_count == len(suggestions):
            sudoku.solutions.append(copy.deepcopy(sudoku.sudoku_square_copy))
            return
        # If suggestions remain, then try the solver again. When new suggestions are computed,
        # there might be some cells that then have only 1 possible value.
        else:
            try_fill_in(sudoku, start_time)

    # At this point the sudoku square either had no empty cells to begin with
    #   or all empty cells have more than 1 option. To solve that another algorithm should be used
    #   Hence, this is a good point to return from
    return
