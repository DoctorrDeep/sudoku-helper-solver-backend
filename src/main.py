from src import example_problems
from src.helpers.generate_problems import create_sudoku_problem
from src.solutions.backtracking_solution import solve, solve_square
from src.sudoku_cube import Sudoku

# Select a sudoku problem
# sudoku = Sudoku(example_problems.MEDIUM_SUDOKU)
sudoku = Sudoku(example_problems.DIFFICULT_SUDOKU)
print(sudoku)
# Get all possible solutions to a sudoku printed in terminal using the backtracking algorithm
sudoku.run_solver(solve_square)
print(sudoku)

# Get all possible solutions to a sudoku printed in terminal using the backtracking algorithm
solve(sudoku.sudoku_square, verbose=True)
print("Completed sudoku")

solved_sudoku = create_sudoku_problem()
solved_sudoku.print_problem()


# # Select a sudoku problem
# sudoku = example_problems.DIFFICULT_SUDOKU
#
# # Get last possible solution
# last_solution = try_fill_in(sudoku)
# print("Correct intermediate solution: ")
# pprint(last_solution)
# print("Options for incomplete cells: ")
# pprint(get_suggestions(last_solution))
