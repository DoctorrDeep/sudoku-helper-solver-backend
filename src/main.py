from pprint import pprint

from src import example_problems
from src.helpers.generate_problems import create_sudoku_problem
from src.solutions.backtracking_solution import solve_square
from src.solutions.no_backtracking_solution import try_fill_in
from src.sudoku_cube import Sudoku

# Select a sudoku problem
sudoku = Sudoku(example_problems.MEDIUM_SUDOKU)
# sudoku = Sudoku(example_problems.DIFFICULT_SUDOKU)
print(sudoku)

# Get all possible solutions to a sudoku printed in terminal using the backtracking algorithm
sudoku.run_solver(solve_square)
print(sudoku)

# Create a sudoku problem and view the unfinished square
solved_sudoku = create_sudoku_problem()
solved_sudoku.print_problem()


# Get last possible solution using no_backtracking
sudoku.run_solver(try_fill_in)
print("Correct intermediate solution: ")
sudoku.print_incomplete_solution()
print("Options for incomplete cells: ")
pprint(sudoku.suggestions)
