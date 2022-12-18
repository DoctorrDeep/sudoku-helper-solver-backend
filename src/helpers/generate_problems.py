import copy
import random

from src.helpers import ALL_XYS
from src.helpers.errors import UnknownSolutionSpace
from src.helpers.timer import timer
from src.solutions.backtracking_solution import solve_square
from src.sudoku_cube import Sudoku

MAX_COUNT_OF_CELLS_TO_EMPTY = 30
MAX_COUNT_OF_SUGGESTIONS_IN_ANY_CELL = 3


@timer
def create_sudoku_problem() -> Sudoku:
    """
    Generate a solved sudoku cube and start removing
    numbers till the highest number of solutions
    to any cell in the full square exceeds 2
    """

    def generate_sudoku_square() -> Sudoku:
        """
        Generate an empty sudoku square and use
        backtracking to fill it in.
        """
        empty_square = [[0] * 9 for _ in range(9)]

        # Randomly fill a few spots in the empty square to generate different problems
        spots_filled = 0
        while spots_filled < 10:
            rand_xy = random.choice(ALL_XYS)
            empty_square[rand_xy[0]][rand_xy[1]] = random.choice(range(1, 10))
            if Sudoku.check_solution(empty_square):
                spots_filled += 1
            else:
                empty_square[rand_xy[0]][rand_xy[1]] = 0

        sudoku = Sudoku(empty_square)
        sudoku.run_solver(solve_square)
        return sudoku

    sudoku_square = generate_sudoku_square()
    if sudoku_square.solutions:
        sudoku_square.sudoku_square = random.choice(sudoku_square.solutions)
    else:
        raise UnknownSolutionSpace("Generated problem with empty solutions.")
    sudoku_square.sudoku_square_copy = copy.deepcopy(sudoku_square.sudoku_square)
    elements_to_empty = random.sample(ALL_XYS, MAX_COUNT_OF_CELLS_TO_EMPTY)
    for loc in elements_to_empty:
        sudoku_square.sudoku_square[loc[0]][loc[1]] = 0
        sudoku_square.sudoku_square_copy[loc[0]][loc[1]] = 0
        if sudoku_square.get_max_suggestions_count() >= MAX_COUNT_OF_SUGGESTIONS_IN_ANY_CELL:
            return sudoku_square

    raise UnknownSolutionSpace(
        "Number of suggestions remains low even after removing %i out of 81 cells" % MAX_COUNT_OF_CELLS_TO_EMPTY
    )
