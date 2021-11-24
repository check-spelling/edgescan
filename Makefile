all: clean test build

clean:
	rm -rf dist

container:
	docker build --tag edgescan --file docker/Containerfile .

update:
	poetry show -o
	poetry update
	poetry export -f requirements.txt -o requirements.txt --without-hashes
	poetry show --tree

test:
	poetry run coverage run -m pytest --durations=0

install:
	poetry install

build: test
	poetry build

release: build
	poetry publish
