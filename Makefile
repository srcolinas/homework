.PHONY: test test-entity test-all coverage install dev setup clean

# Python configuration
PYTHON := python3.12
UV := uv

# Project paths
SRC_DIR := src
TEST_DIR := tests

# Default target
.DEFAULT_GOAL := help

# Help command
help:
	@echo "Homework Project Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make test         Run all tests"
	@echo "  make coverage     Run tests with coverage report"
	@echo "  make install      Install project dependencies"
	@echo "  make dev          Install development dependencies"
	@echo "  make clean        Clean cache files"
	@echo "  make setup        Setup development environment"

# Install project dependencies
install:
	$(UV) pip install -e .

# Install development dependencies
dev:
	$(UV) pip install -e ".[dev]"

# Setup development environment
setup: clean
	$(UV) venv --python $(PYTHON)
	make dev

# Run all tests
test:
	$(UV) run -m pytest $(TEST_DIR)

# Run tests with coverage report
test-coverage:
	$(UV) run -m pytest --cov=src/cner

# Run formatting and type checking
lint:
	$(UV) run ruff format .
	$(UV) run ruff check . --fix
	$(UV) run mypy . --check-untyped-defs

# Clean cache files
clean:
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf __pycache__
	rm -rf $(SRC_DIR)/__pycache__
	rm -rf $(SRC_DIR)/**/__pycache__
	rm -rf $(TEST_DIR)/__pycache__
	rm -rf $(TEST_DIR)/.pytest_cache
	rm -rf $(TEST_DIR)/**/__pycache__
	rm -rf .mypy_cache
	rm -rf $(SRC_DIR)/homework.egg-info
	rm -rf dist
	rm -rf .vscode