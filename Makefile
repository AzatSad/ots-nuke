MAKEFLAGS += --silent

.PHONY: run
run:
	poetry run python -m ots_nuke

.PHONY: down
down:
	pkill -f "uvicorn" || true

.PHONY: lint
lint:
	poetry run ruff format ./ \
	&& poetry run ruff check ./

.PHONY: mypy
mypy:
	poetry run mypy .

.PHONY: pre-commit
pre-commit:
	make lint && make mypy

.PHONY: tests
tests:
	poetry run pytest ./tests/

.PHONY: cov
cov:
	poetry run pytest --cov=ots_nuke ./tests

.PHONY: cov-html
cov-html:
	poetry run pytest --cov=ots_nuke ./tests --cov-report=html

.PHONY: all
all:
	make pre-commit && make tests && echo "All checks passed!"

pc: pre-commit
t: tests