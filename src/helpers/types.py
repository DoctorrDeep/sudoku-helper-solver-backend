from enum import Enum

SudokuRow = list[int]
SudokuSquare = list[SudokuRow]
SudokuSuggestions = dict[tuple[int, int], list[int]]
SudokuSuggestionsModel = dict[str, list[int]]


class Level(Enum):
    easy = "easy"
    difficult = "difficult"
