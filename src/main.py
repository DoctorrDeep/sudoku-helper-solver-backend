from fastapi import FastAPI

from src.helpers.generate_problems import create_sudoku_problem
from src.helpers.types import Level, SudokuSquare, SudokuSuggestionsModel
from src.solutions.backtracking_solution import solve_square
from src.solutions.no_backtracking_solution import try_fill_in
from src.sudoku_cube import Sudoku

app = FastAPI()


@app.get("/")
async def health_check():
    return {"status": "ok"}


@app.get("/create/{level}", response_model=SudokuSquare)
async def create_sudoku(level: Level) -> SudokuSquare:
    """Create a sudoku problem and view the unfinished square"""
    solved_sudoku = create_sudoku_problem(level)
    solved_sudoku.print_problem()
    solved_sudoku.print_suggestions()
    return solved_sudoku.sudoku_square


@app.post("/hints", response_model=SudokuSuggestionsModel)
async def create_hints_for_sudoku(sudoku_square: SudokuSquare):
    """Get suggestions for all empty cells in a sudoku square"""
    suggestions = Sudoku(sudoku_square).suggestions
    tuple_only_dict = {",".join([str(i) for i in k]): v for k, v in suggestions.items()}
    return tuple_only_dict


@app.post("/solve", response_model=SudokuSquare)
async def get_solution(sudoku_square: SudokuSquare):
    """Solve an incomplete sudoku square"""
    sudoku = Sudoku(sudoku_square)
    sudoku.run_solver(solve_square)
    return sudoku.solutions[0]


@app.post("/harder", response_model=SudokuSquare)
async def complete_easy_cells(sudoku_square: SudokuSquare):
    """Fill in the cells of a square that have one solution only"""
    sudoku = Sudoku(sudoku_square)
    sudoku.run_solver(try_fill_in)
    return sudoku.sudoku_square_copy
