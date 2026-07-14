# === Configuration ===
MAKEFLAGS += --silent

.PHONY: make
make:
	cat -n ./Makefile

# === Build ===
.PHONY: dc-build
dc-build:
	docker compose up --build

.PHONY: dc-up
dc-up:
	docker compose up

.PHONY: dc-up-d
dc-up-d:
	docker compose up -d

.PHONY: dc-down
dc-down:
	docker compose down

.PHONY: run
run:
	poetry run python -m ots_nuke

.PHONY: down
down:
	pkill -f "uvicorn" || true

# === Lint ===
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

# === Tests ===
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