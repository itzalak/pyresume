# Makefile

VENV = .venv

install: poetry-local-venv python-delete-venv poetry-install

poetry-install:
	@echo "creating venv and installing dependencies"
	poetry install

python-delete-venv:
	@echo "removing existent virtualenv"
	rm -rf $(VENV)
	rm -rf venv

poetry-local-venv:
	@echo "setting virtualenv location to project"
	poetry config virtualenvs.in-project true

poetry-get-env:
	poetry env info --path

poetry-update:
	poetry update

poetry-test:
	poetry run pytest

# Pre-commit configuration
pre-commit: setup-pre-commit update-pre-commit

setup-pre-commit:
	pre-commit install

update-pre-commit:
	pre-commit autoupdate

# Create resume
resume-bar:
	poetry run python pyresume/__main__.py -bar

resume-simple:
	poetry run python pyresume/__main__.py -simple

resume-divider:
	poetry run python pyresume/__main__.py -divider
