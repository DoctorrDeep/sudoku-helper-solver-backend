# Sudoku Helper Solver

## Purpose of project

## How to run

- run on python 3.10.4 and up
```bash
pyenv shell 3.10.4
poetry env use python3.10
poetry install
poetry shell
python src/visualizer/visualize_sudoku_solution.py
```
  - at present this shows how far we get with the non-backtracking algorithm

## Inspiration

I was watching a video on sudoku solver with python on Youtube when I realised that this is probably a simple problem. This [Computerphile video](https://www.youtube.com/watch?v=G_UYXzGuqvM) talks about backtracking algorithms which I did not follow at the time.

Cut to two weeks later, I am still thinking of the video. I find myself attempting to actually do Sudoku problems. Since this is an interesting problem and I often need help to solve the difficult problems, I started thinking of writing a script to solve it.

The challenge is to NOT watch the video again or research any type of backtracking algorithm.

## How the project is arranged

- `visualize_sudoku_solution.py`
  - this needs a sudoku square as input, which it gets from `starter_sudoku_sets.py`
  - it uses one of the solvers
    - `no_backtracking_solution.py` --> Hardcoded to be used everytime
    - `backtracking_solution.py` --> Not Implemented

## TODO

- Make pytests/doctests for all functions
- Make REST service out of the solver with
  - endpoint for hints when a problem is sent
  - endpoint for solutions when a problem is sent
- drop cli
- Make pygame flip between initial problem and presented solution periodically
- Implement gitflow to run tests
- Make each iteration of recursion visual, make it pretty
