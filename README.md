# Sudoku Helper Solver

## Purpose of project

## How to run

- run on python 3.10.4 and up
```bash
pyenv shell 3.10.4
poetry env use python3.10
poetry install
poetry shell
```
- run help file to understand/debug app
```bash
python src/visualizer/help.py
```
- run local server for development
```bash
uvicorn src.main:app --reload
```
- then visit [http://127.0.0.1:8000](http://127.0.0.1:8000) for normal api
- and [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for OpenAPI docs

## Inspiration

I was watching a video on sudoku solver with python on Youtube when I realised that this is probably a simple problem. This [Computerphile video](https://www.youtube.com/watch?v=G_UYXzGuqvM) talks about backtracking algorithms which I did not follow at the time.

Cut to two weeks later, I am still thinking of the video. I find myself attempting to actually do Sudoku problems. Since this is an interesting problem and I often need help to solve the difficult problems, I started thinking of writing a script to solve it.

The challenge is to NOT watch the video again or research any type of backtracking algorithm.



## TODO

 #### Deprecated

- Make pygame flip between initial problem and presented solution periodically
- Make each iteration of recursion visual, make it pretty


#### Active

- ~~run ALL linters and tests through GH actions~~
- ~~All solvers to use the Sudoku class, remove, non class solvers~~
- ~~move get_suggestions to class method~~
- ~~Make pytests for all functions~~
- ~~convert cli + pygame into help-only state, i.e. not deleted, but hidden and not run unless local+explicit~~
- Make REST service out of the use cases using FastAPI with the following requests
  - ~~endpoint to create a new problem (create, as endpoint)~~
  - ~~endpoint for hints when a problem is sent (hints, as endpoint)~~
  - ~~endpoint for solutions when a problem is sent (solve, as endpoint)~~
  - ~~Add better Documents/example body~~
  - ~~handle exceptions~~
  - ~~set timeouts for difficult problem creation~~
  - write rest-api tests
- Terraform code to deploy
  - dockerize app?
- Link to React App locally
