install:
	poetry install

test:
	poetry run pytest gendiff tests/tests.py

lint:
	poetry run flake8 --show-source gendiff --ignore=I002,WPS515,T001,WPS210,WPS231

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: install test lint selfcheck check build