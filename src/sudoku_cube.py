import copy
from typing import Callable

from src.helpers import CUBE_XYS
from src.helpers.suggestions import get_suggestions
from src.helpers.timer import timer
from src.helpers.types import SudokuRow, SudokuSquare


class Sudoku:
    def __init__(self, sudoku_square: SudokuSquare):
        self.sudoku_square = sudoku_square
        self.sudoku_square_copy: SudokuSquare = copy.deepcopy(sudoku_square)
        self.solutions: list[SudokuSquare] = []
        self.suggestions: dict[tuple[int, int], list[int]] = get_suggestions(sudoku_square)

    @staticmethod
    def check_solution(sudoku_square: SudokuSquare) -> bool:
        """
        Check if the given sudoku square is not breaking the following rule
        Each column, row, predefined 3X3 square should have
        - numbers 1 to 9
        - no repeats

        Returns boolean of whether all of the above are
        - satisfied (True) OR
        - not satisfied (False)
        """

        # Check all rows
        for row in sudoku_square:
            if not Sudoku.check(row):
                return False

        # Check all columns
        for i in range(9):
            temp = []
            for row in sudoku_square:
                temp.append(row[i])
            if not Sudoku.check(temp):
                return False

        # Check all predefined 3x3 cubes
        for cube_xy in CUBE_XYS:
            cube_list = [sudoku_square[xy[0]][xy[1]] for xy in cube_xy]
            if not Sudoku.check(cube_list):
                return False

        # Since all 3 have not returned False, all checks must have passed
        return True

    @staticmethod
    def check(nums: SudokuRow) -> bool:
        """
        Given a list of numbers, this function checks
        - all non-zero numbers are between 1 and 9
        - all non-zero numbers are mentioned only once
        - all non-zero numbers are integers

        Returns boolean of whether all of the above are
        - satisfied (True) OR
        - not satisfied (False)
        """
        nums = [i for i in nums if i]  # remove zeros/Nones
        unique = len(set(nums)) == len(nums)
        if not unique:
            return False

        for i in nums:
            if not (0 < i < 10 and isinstance(i, int)):
                return False

        return True

    def strict_check(self, nums: SudokuRow) -> bool:
        """
        Extends check method above with strict checks
        for presence of empty(value 0) cells.
        TODO: Remove if unnecessary/unused
        """
        if all(nums):
            return self.check(nums)
        return False

    @timer
    def run_solver(self, solver_func: Callable):
        solver_func(self)
        return None

    def __str__(self):
        if len(self.solutions) > 0:
            return "solution\n" + "\n".join([str(i) for i in self.solutions]) + "\nend of solution"
        return "problem\n" + "\n".join([str(i) for i in self.sudoku_square_copy]) + "\nend of problem"

    def print_problem(self):
        print("problem\n" + "\n".join([str(i) for i in self.sudoku_square_copy]) + "\nend of problem")
