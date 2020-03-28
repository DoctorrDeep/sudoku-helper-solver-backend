import copy
from pprint import pprint
from itertools import product

from typing import Dict, List, Optional, Set

import starter_sudoku_sets

# Define 3X3 squares in grid
cube_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

cube_xys = []
for x_and_y in product(cube_list, cube_list):
    a_cube = []
    for xy in product(x_and_y[0], x_and_y[1]):
        a_cube.append(xy)
    cube_xys.append(a_cube)

# Define 3X3 squares in grid: with list comprehension (less readable)
# cube_xys = [
#     [xy for xy in product(x_and_y[0], x_and_y[1])]
#     for x_and_y in product(cube_list, cube_list)
# ]

# Define array of ALL cell positions in sudoku grid
all_xys = list(product(range(9), range(9)))


def do_check(nums: List[int]) -> bool:
    """
    Given a list of numbers, this function checks
    - all non-zero numbers are mentioned only once
    - all non-zero numbers are between 1 and 9
    - all non-zero numbers are integers

    Returns boolean of whether all of the above are satisfied (True) or not (False)
    """
    zero_remover = lambda a_list: [i for i in a_list if i]
    nums = zero_remover(nums)
    unique = len(set(nums)) == len(nums)
    correct = True
    for i in nums:
        if i > 0 and i < 10 and isinstance(i, int):
            correct = True
        else:
            correct = False
            break

    return unique and correct


def check_solution(sudoku_square: List[List[int]]) -> bool:
    """
    Check if the given sudoku square is not breaking the following rule
    Each column, row, predefined 3X3 square should have numbers 1 to 9, no repeats

    Returns boolean of whether all of the above are satisfied (True) or not (False)
    """

    # Check that all rows
    check_hor = True
    for row in sudoku_square:
        check_hor = check_hor and do_check(row)

    # Check that all columns
    check_ver = True
    for i in range(9):
        temp = []
        for row in sudoku_square:
            temp.append(row[i])
        check_ver = check_ver and do_check(temp)

    # Check all predefined 3x3 square
    check_cubes = True
    for cube_xy in cube_xys:
        a_cube = [sudoku_square[xy[0]][xy[1]] for xy in cube_xy]
        check_cubes = check_cubes and do_check(a_cube)

    # Combine all 3 results from above
    return check_hor and check_ver and check_cubes


def try_fill_in(
    sudoku_square: List[List[int]],
    sudoku_dict: Optional[Dict[Set[int], List[int]]] = {},
):
    """
    Attempts will be made to fill in given sudoku square.

    Returns:
    - as much filled in sudoku square
    - options in rest of cells
    """

    found_a_solution = False
    print("received Sudoku square:")
    pprint(sudoku_square)

    # loop over all cells in sudoku square
    for xy in all_xys:
        if not sudoku_square[xy[0]][xy[1]]:
            temp_sudoku = copy.deepcopy(sudoku_square)
            temp_values = []

            # try each of the allowed numbers in chosen cell
            for i in range(1, 10):
                temp_sudoku[xy[0]][xy[1]] = i
                if check_solution(temp_sudoku):
                    temp_values.append(i)

            sudoku_dict[xy] = temp_values

    # Update sudoku square with found solutions
    for xy, sudo_val in sudoku_dict.items():
        if len(sudo_val) == 1:
            found_a_solution = True
            sudoku_square[xy[0]][xy[1]] = sudo_val[0]

    # Remove unique solutions after updating sudoku square
    if sudoku_dict:
        keys_to_del = [key for key, val in sudoku_dict.items() if len(val) == 1]
        for key in keys_to_del:
            del sudoku_dict[key]

    # Make recursive call with new sudoku square as input
    if found_a_solution:
        try_fill_in(sudoku_square)

    ## Experimental stuff that did not work.
    ## Backtracking needs to be implemented.
    # else:
    #     all_items = lambda a_dict: [i for key, val in a_dict.items() for i in val]
    #     if all_items(sudoku_dict):
    #         xy = list(sudoku_dict.keys())[0]
    #         for a_option in sudoku_dict[xy]:
    #             temp_sudoku = copy.deepcopy(sudoku_square)
    #             temp_sudoku[xy[0]][xy[1]] = a_option
    #             print(f"Trying new solution with {a_option} in {xy}")
    #             pprint(temp_sudoku)
    #             input("Continue?")
    #             try_fill_in(temp_sudoku)

    return sudoku_square, sudoku_dict


if __name__ == "__main__":

    # Select a sudoku problem
    sudoku = starter_sudoku_sets.difficult_sudoku

    # Get last possible solution
    last_solution, sudoku_dict = try_fill_in(sudoku)
    print("Correct intermediate solution: ")
    pprint(last_solution)
