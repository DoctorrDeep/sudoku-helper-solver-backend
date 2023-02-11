from ambars_sudoku_solver.helpers.generate_problems import create_sudoku_problem
from ambars_sudoku_solver.helpers.types import (
    Level,
    SudokuSquare,
    SudokuSuggestionsModel,
)
from ambars_sudoku_solver.solvers.backtracking_solution import solve_square
from ambars_sudoku_solver.solvers.no_backtracking_solution import try_fill_in
from ambars_sudoku_solver.sudoku_cube import Sudoku
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health_check():
    return {
        "status": "ok",
        "docs": {"local": "http://0.0.0.0:8000/docs", "production": "https://ambardas.nl:8000/docs"},
    }


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
    if not Sudoku.check_solution(sudoku_square):
        raise HTTPException(status_code=400, detail="Problem set wrongly and will not be solved")
    sudoku = Sudoku(sudoku_square)
    sudoku.run_solver(solve_square)
    return sudoku.solutions[0]


@app.post("/harder", response_model=SudokuSquare)
async def complete_easy_cells(sudoku_square: SudokuSquare):
    """Fill in the cells of a square that have one solution only"""
    sudoku = Sudoku(sudoku_square)
    sudoku.run_solver(try_fill_in)
    return sudoku.sudoku_square_copy
