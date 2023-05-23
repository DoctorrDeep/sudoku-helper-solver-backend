# Sudoku Helper Solver

## Purpose of project

- Personal project to experiment with stuff
- Look like you know what you are talking about
- Who am I kidding? Is anyone even reading item number 3 in in a "purpose" list?

## How to run locally : BARE

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

## How to run locally : Inside a Docker container

- `make build DOCKER_TAG=v1.0`: This will build the docker image, provided you can run make files and have docker installed
- `make run DOCKER_TAG=v1.0`: This will run the built image in detached mode
- At this stage, you have the following options:
  - Visit [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs) to visit and interact with the API
  - Look up the logs of the applicaton using `docker logs -tf sudoku_solver_fastapi`
  - Get inside the container `docker exec -it sudoku_solver_fastapi bash`
- `make clean`: To stop and remove the container
- `make clean-image DOCKER_TAG=v1.0`: To remove the docker image

## Build and push image to docker-hub

- login to docker-cli: `docker login -u <YOUR_DOCKERHUB_USERNAME>`
    - notes:
    - your local gpg key may/maynot be valid right now
    - have the passphrase key handy
- `make docker-push DOCKER_TAG=v1.0`

## Inspiration

I was watching a video on sudoku solver with python on Youtube when I realised that this is probably a simple problem. This [Computerphile video](https://www.youtube.com/watch?v=G_UYXzGuqvM) talks about backtracking algorithms which I did not follow at the time.

Cut to two weeks later, I am still thinking of the video. I find myself attempting to actually do Sudoku problems. Since this is an interesting problem and I often need help to solve the difficult problems, I started thinking of writing a script to solve it.

The challenge is to NOT watch the video again or research any type of backtracking algorithm.

## TODO

#### Active

- ~~Better tagging of docker images i.e. no hard-coding~~
- ~~Push to a docker repository. Use that pipeline instead of doing `docker save` here and `docker load` at the infra-as-code codebase~~
- Deprecate makefile calls to save+zip docker image
- create a service that saves incomplete sudoku grids (i.e. problems) into a postgres/sqlite DB using dqlalchemy
- create background tasks that check and generate sudoku problems and save to aforementioned DB
- make a new endpoint that serves problems from the DB and starts background tasks to cleanup/create new rows in DB
- use redis/celery to manage tasks?
- use docker-compose instead of docker run to build images and save to dockerhub

#### Deprecated

- Make pygame flip between initial problem and presented solution periodically
- Make each iteration of recursion visual, make it pretty
