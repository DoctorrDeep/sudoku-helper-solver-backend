from ambars_sudoku_solver.helpers.types import Level, SudokuSquare

from src.db.db_setup import Session
from src.db.models import Problem


def add_problem(difficulty: Level, problem: SudokuSquare):
    with Session.begin() as session:
        session.add(Problem(difficulty=difficulty, problem=problem))
        session.commit()


def get_problem(difficulty: Level) -> SudokuSquare:
    with Session.begin() as session:
        problem = session.query(Problem).filter(Problem.difficulty == difficulty)

        # TODO: Start background task to
        #  - remove the current problem from the DB
        #  - generate a new problem of the same type and add to the DB

        return problem
