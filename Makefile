install:
	poetry install

test:
	poetry run pytest -vv --cov=gendiff --cov-report xml tests/tests.py

lint:
	poetry run flake8 gendiff --show-source --ignore=I002,WPS515,T001,WPS210,WPS231,W291,E126,E101,E131,WPS232,W292,E501 --verbose

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: install test lint selfcheck check build
