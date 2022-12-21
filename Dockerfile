FROM ubuntu:latest

RUN apt update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev git

ENV HOME="/root"
ENV PYTHON_VERSION=3.10.4

# Set the working directory to root
WORKDIR ${HOME}

#Install and setup Pyenv
RUN curl https://pyenv.run | bash
ENV PYENV_ROOT=${HOME}/.pyenv
ENV PATH=${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}

RUN pyenv install ${PYTHON_VERSION} -v
RUN pyenv global ${PYTHON_VERSION}


# Set the working directory to the project directory
WORKDIR /app

# Add the project files to the image
ADD src /app/src
ADD pyproject.toml /app
ADD poetry.lock /app

# Install the project dependencies
RUN ${HOME}/.pyenv/versions/3.10.4/bin/pip install poetry
RUN ${HOME}/.pyenv/versions/3.10.4/bin/python -m poetry install --no-dev

# Expose the default port
EXPOSE 80

# Set the entrypoint to run the Flask app
ENTRYPOINT ["/root/.pyenv/versions/3.10.4/bin/python", "-m","poetry", "run", "uvicorn", "src.main:app", "--port", "80", "--host", "0.0.0.0"]
