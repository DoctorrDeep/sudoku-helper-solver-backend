"""Make checks that various functions need to check rules"""
import copy
from itertools import product
from typing import Dict, List, Set

# Define 3X3 squares in grid
cube_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

cube_xys = []
for x_and_y in product(cube_list, cube_list):
    a_cube = []
    for row_col in product(x_and_y[0], x_and_y[1]):
        a_cube.append(row_col)
    cube_xys.append(a_cube)

# Define 3X3 squares in grid: with list comprehension (less readable)
# cube_xys = [
#     [row_col for row_col in product(x_and_y[0], x_and_y[1])]
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

    Returns boolean of whether all of the above are
    - satisfied (True) OR
    - not satisfied (False)
    """

    # lambdas not allowed in this format in pep8
    # zero_remover = lambda a_list: [i for i in a_list if i]
    # nums = zero_remover(nums)

    nums = [i for i in nums if i]
    unique = len(set(nums)) == len(nums)
    correct = True
    for i in nums:
        if 0 < i < 10 and isinstance(i, int):
            correct = True
        else:
            correct = False
            break

    return unique and correct


def check_solution(sudoku_square: List[List[int]]) -> bool:
    """
    Check if the given sudoku square is not breaking the following rule
    Each column, row, predefined 3X3 square should have
    - numbers 1 to 9
    - no repeats

    Returns boolean of whether all of the above are
    - satisfied (True) OR
    - not satisfied (False)
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
        cube = [sudoku_square[xy[0]][xy[1]] for xy in cube_xy]
        check_cubes = check_cubes and do_check(cube)

    # Combine all 3 results from above
    return check_hor and check_ver and check_cubes


def get_suggestions(sudoku_square: List[List[int]]) -> Dict[Set[int], List[int]]:
    """
    Loop over all cells and for each cell get list of possible options
    """

    suggestions = dict()

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

            suggestions[xy] = temp_values

    return suggestions
