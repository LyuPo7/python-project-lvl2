install:
	poetry install

test:
	poetry run pytest -vv --cov=gendiff --cov-report xml tests/tests.py

lint:
	poetry run flake8 gendiff --show-source --ignore=E131 --verbose

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: install test lint selfcheck check build
