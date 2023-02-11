"""This file helps onboard users and debug issues. No function benefit during runtime."""
from pprint import pprint

from ambars_sudoku_solver.helpers.generate_problems import create_sudoku_problem
from ambars_sudoku_solver.helpers.types import Level
from ambars_sudoku_solver.solutions.backtracking_solution import solve_square
from ambars_sudoku_solver.solutions.no_backtracking_solution import try_fill_in
from ambars_sudoku_solver.sudoku_cube import Sudoku

from src.visualizer import example_problems

# Select a sudoku problem
sudoku = Sudoku(example_problems.MEDIUM_SUDOKU)
# sudoku = Sudoku(example_problems.DIFFICULT_SUDOKU)
print(sudoku)


# Get all possible solutions to a sudoku printed in terminal using the backtracking algorithm
sudoku.run_solver(solve_square)
print(sudoku)


# Create a sudoku problem and view the unfinished square
solved_sudoku = create_sudoku_problem(Level.easy)
solved_sudoku.print_problem()
solved_sudoku.print_suggestions()


# Get last possible solution using no_backtracking
sudoku.run_solver(try_fill_in)
print("Correct intermediate solution: ")
sudoku.print_incomplete_solution()
print("Options for incomplete cells: ")
pprint(Sudoku.get_suggestions(sudoku.sudoku_square_copy))
