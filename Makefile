build:
	@docker network inspect sudoku_solver_net.local >/dev/null 2>&1 || \
	  		docker network create -d bridge sudoku_solver_net.local
	@docker build -t sudoku_solver_img:v1.0 -f Dockerfile .


run:
	@docker run --name=sudoku_solver_fastapi \
				--network=sudoku_solver_net.local \
				--rm=true \
				-p 8000:8000 \
				-itd sudoku_solver_img:v1.0

save:
	@docker save sudoku_solver_img:v1.0 | gzip > sudoku_solver_img.tar.gz

run-from-saved-image:
	@docker load -i sudoku_solver_img.tar.gz

clean:
	@docker rm -f sudoku_solver_fastapi

clean-image:
	@docker rmi sudoku_solver_img:v1.0
