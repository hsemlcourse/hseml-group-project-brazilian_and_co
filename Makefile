install:
	pip install -r requirements.txt

install-hooks:
	pre-commit install

lint:
	flake8 .
	ruff check .

run-hooks:
	pre-commit run --all-files