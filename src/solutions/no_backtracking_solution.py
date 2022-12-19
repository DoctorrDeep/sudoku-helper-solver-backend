"""Solve Sudoku using recursion only"""
import copy

from src.sudoku_cube import Sudoku


def try_fill_in(sudoku: Sudoku):
    """
    Attempts will be made to fill in given sudoku square where only 1 suggestion is to be had
    """

    found_a_solution = False
    used_suggestions_count = 0
    suggestions = Sudoku.get_suggestions(sudoku.sudoku_square_copy)  # Calculate suggestions in latest state

    # Update sudoku square with found solutions
    for xy, sudo_val in suggestions.items():
        if len(sudo_val) == 1:
            found_a_solution = True
            used_suggestions_count += 1
            sudoku.sudoku_square_copy[xy[0]][xy[1]] = sudo_val[0]

    if found_a_solution:
        # If all suggestions have been used up, then return from solver
        if used_suggestions_count == len(suggestions):
            sudoku.solutions.append(copy.deepcopy(sudoku.sudoku_square_copy))
            return
        # If suggestions remain, then try the solver again. When new suggestions are computed,
        # there might be some cells that then have only 1 possible value.
        else:
            try_fill_in(sudoku)

    # At this point the sudoku square either had no empty cells to begin with
    #   or all empty cells have more than 1 option. To solve that another algorithm should be used
    #   Hence, this is a good point to return from
    return
