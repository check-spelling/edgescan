FROM python:3.9-slim-bullseye

#: Install poetry and gcc.
RUN apt-get update
RUN apt-get -y install --no-install-recommends apt-utils gcc g++ make
RUN pip install poetry

WORKDIR /app

#: Install dependencies.
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev

#: Install everything else.
COPY . .
RUN poetry install --no-dev
