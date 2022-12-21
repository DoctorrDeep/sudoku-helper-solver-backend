class UnknownSolutionError(Exception):
    """Raise when the solution to a sudoku problem cannot be found"""

    def __init__(self, message):
        self.message = message


class SolverTimeoutError(Exception):
    """Raise when it is taking too long to complete a solver"""

    def __init__(self, message):
        self.message = message
