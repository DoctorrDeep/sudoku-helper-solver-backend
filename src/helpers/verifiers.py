"""Make checks that various functions need to check rules"""
from . import CUBE_XYS


def do_check(nums: list[int]) -> bool:
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
        if not (0 < i < 10 and isinstance(i, int)):
            correct = False
            break

    return unique and correct


def check_solution(sudoku_square: list[list[int]]) -> bool:
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
    for cube_xy in CUBE_XYS:
        cube = [sudoku_square[xy[0]][xy[1]] for xy in cube_xy]
        check_cubes = check_cubes and do_check(cube)

    # Combine all 3 results from above
    return check_hor and check_ver and check_cubes
