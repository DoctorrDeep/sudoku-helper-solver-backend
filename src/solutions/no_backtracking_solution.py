"""Solve Sudoku using recursion only"""
import copy

from src.sudoku_cube import Sudoku


def try_fill_in(sudoku: Sudoku):
    """
    Attempts will be made to fill in given sudoku square where only 1 suggestion is to be had
    """

    found_a_solution = False

    # Update sudoku square with found solutions
    for xy, sudo_val in sudoku.suggestions.items():
        if len(sudo_val) == 1:
            found_a_solution = True
            sudoku.sudoku_square_copy[xy[0]][xy[1]] = sudo_val[0]

    # Remove unique solutions after updating sudoku square
    if sudoku.suggestions:
        del_keys = [key for key, val in sudoku.suggestions.items() if len(val) == 1]
        for key in del_keys:
            del sudoku.suggestions[key]

    if found_a_solution:
        # update suggestions dict
        sudoku.get_suggestions()
        # If the square is full, then return from function
        if sudoku.check_solution(sudoku.sudoku_square_copy, strict=True):
            sudoku.solutions.append(copy.deepcopy(sudoku.sudoku_square_copy))
            return
        else:
            # Make recursive call with updated sudoku square as input
            try_fill_in(sudoku)
