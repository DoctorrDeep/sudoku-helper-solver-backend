import copy
from pprint import pprint
from typing import Callable

from src.helpers import ALL_XYS, CUBE_XYS
from src.helpers.timer import timer
from src.helpers.types import SudokuRow, SudokuSquare, SudokuSuggestions


class Sudoku:
    def __init__(self, sudoku_square: SudokuSquare):
        self.sudoku_square = sudoku_square
        self.sudoku_square_copy: SudokuSquare = copy.deepcopy(sudoku_square)
        self.solutions: list[SudokuSquare] = []
        self.suggestions: SudokuSuggestions = Sudoku.get_suggestions(sudoku_square)

    def update_suggestions(self):
        self.suggestions = Sudoku.get_suggestions(self.sudoku_square)

    def get_max_suggestions_count(self) -> int:
        return max([len(i) for i in self.suggestions.values()])

    @staticmethod
    def get_suggestions(sudoku_square: SudokuSquare) -> SudokuSuggestions:
        """
        Loop over all cells and for each empty cell get list of possible options
        """
        suggestions = dict()

        # loop over all cells in sudoku square
        for xy in ALL_XYS:
            if not sudoku_square[xy[0]][xy[1]]:
                temp_values = []

                # try each of the allowed numbers in chosen cell
                for i in range(1, 10):
                    sudoku_square[xy[0]][xy[1]] = i
                    if Sudoku.check_solution(sudoku_square):
                        temp_values.append(i)
                    sudoku_square[xy[0]][xy[1]] = 0

                suggestions[xy] = temp_values
        return suggestions

    @staticmethod
    def check_solution(sudoku_square: SudokuSquare, strict: bool = False) -> bool:
        """
        Check if the given sudoku square is not breaking the following rule
        Each column, row, predefined 3X3 square should have
        - numbers 1 to 9
        - no repeats

        Returns boolean of whether all of the above are
        - satisfied (True) OR
        - not satisfied (False)
        """

        check = Sudoku.strict_check if strict else Sudoku.check

        # Check all rows
        for row in sudoku_square:
            if not check(row):
                return False

        # Check all columns
        for i in range(9):
            temp = []
            for row in sudoku_square:
                temp.append(row[i])
            if not check(temp):
                return False

        # Check all predefined 3x3 cubes
        for cube_xy in CUBE_XYS:
            cube_list = [sudoku_square[xy[0]][xy[1]] for xy in cube_xy]
            if not check(cube_list):
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

    @staticmethod
    def strict_check(nums: SudokuRow) -> bool:
        """
        Extends check method above with strict checks
        for presence of empty(value 0) cells.
        TODO: Remove method. This methods use keeps getting refactored away!
        """
        if all(nums):
            return Sudoku.check(nums)
        return False

    @timer
    def run_solver(self, solver_func: Callable):
        solver_func(self)
        return None

    def __str__(self):
        if len(self.solutions) > 0:
            return "solution\n" + "\n".join([str(i) for i in self.solutions]) + "\nend of solution"
        return "problem\n" + "\n".join([str(i) for i in self.sudoku_square]) + "\nend of problem"

    def print_problem(self):
        print("problem")
        pprint(self.sudoku_square)
        print("end of problem")

    def print_incomplete_solution(self):
        print("last attempt at fill in")
        pprint(self.sudoku_square_copy)
        print("end of last attempt at fill in")

    def print_suggestions(self):
        print("suggestions dict")
        pprint(self.suggestions)
        print("end of suggestions dict")
