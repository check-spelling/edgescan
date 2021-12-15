all: clean test build

clean:
	rm -rf dist

container:
	docker build --tag edgescan --file docker/Containerfile .

update:
	poetry export -f requirements.txt -o requirements.txt --without-hashes

test:
	poetry run coverage run -m pytest --durations=0
	poetry run coverage report

install:
	poetry install

build:
	poetry build

release: build
	poetry publish
