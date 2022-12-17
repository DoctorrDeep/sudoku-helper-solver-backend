import copy

from src.helpers.verifiers import check_solution

from . import ALL_XYS
from .types import SudokuSquare


def get_suggestions(sudoku_square: SudokuSquare) -> dict[tuple[int, int], list[int]]:
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


def get_max_suggestions_count(sudoku_square: list[list[int]]) -> int:
    suggestions_dict = get_suggestions(sudoku_square)
    suggestions_counts = [len(i) for i in suggestions_dict.values()]
    return max(suggestions_counts)
