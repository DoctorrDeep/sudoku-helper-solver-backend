"""Solve Sudoku using recursion only"""
from pprint import pprint
from typing import List

from verifiers import get_suggestions
import starter_sudoku_sets


def try_fill_in(sudoku_square: List[List[int]]) -> List[List[int]]:
    """
    Attempts will be made to fill in given sudoku square.

    Returns:
    - as much filled in sudoku square
    - options in rest of cells
    """

    found_a_solution = False
    print("received Sudoku square:")
    pprint(sudoku_square)

    # get all possible values for each cell whille following the rules
    sudoku_dict = get_suggestions(sudoku_square)

    # Update sudoku square with found solutions
    for xy, sudo_val in sudoku_dict.items():
        if len(sudo_val) == 1:
            found_a_solution = True
            sudoku_square[xy[0]][xy[1]] = sudo_val[0]

    # Remove unique solutions after updating sudoku square
    if sudoku_dict:
        del_keys = [key for key, val in sudoku_dict.items() if len(val) == 1]
        for key in del_keys:
            del sudoku_dict[key]

    # Make recursive call with new sudoku square as input
    if found_a_solution:
        try_fill_in(sudoku_square)

    return sudoku_square


if __name__ == "__main__":

    # Select a sudoku problem
    sudoku = starter_sudoku_sets.DIFFICULT_SUDOKU

    # Get last possible solution
    last_solution = try_fill_in(sudoku)
    print("Correct intermediate solution: ")
    pprint(last_solution)
    print("Options for incomplete cells: ")
    pprint(get_suggestions(last_solution))
