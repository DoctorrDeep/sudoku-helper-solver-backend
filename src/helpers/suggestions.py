import copy

from src.helpers.cube_locations_mapping import ALL_XYS
from src.helpers.verifiers import check_solution


def get_suggestions(sudoku_square: list[list[int]]) -> dict[set[int], list[int]]:
    """
    Loop over all cells and for each cell get list of possible options
    """
    suggestions = dict()

    # loop over all cells in sudoku square
    for xy in ALL_XYS:
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
