install:
	poetry install

lint:
	poetry run flake8 --show-source gendiff --ignore=I002,WPS515,T001,WPS210,WPS231

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

.PHONY: install lint selfcheck check build