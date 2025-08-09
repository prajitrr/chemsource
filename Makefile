# Makefile for chemsource testing and development

.PHONY: test test-quick test-integration test-unit install-dev clean help

# Default target
help:
	@echo "Available targets:"
	@echo "  test          - Run all tests"
	@echo "  test-quick    - Run quick installation verification"
	@echo "  test-integration - Run integration tests only"
	@echo "  test-unit     - Run unit tests only"
	@echo "  install-dev   - Install package in development mode"
	@echo "  clean         - Clean up test artifacts"
	@echo "  help          - Show this help message"

# Run all tests
test:
	@echo "Running all tests..."
	python tests/run_tests.py

# Quick installation verification
test-quick:
	@echo "Running quick installation verification..."
	python tests/run_tests.py --quick

# Integration tests only
test-integration:
	@echo "Running integration tests..."
	python tests/run_tests.py --integration

# Unit tests only (exclude integration tests)
test-unit:
	@echo "Running unit tests..."
	python -m unittest discover tests -p "test_*.py" -v

# Install package in development mode
install-dev:
	@echo "Installing package in development mode..."
	pip install -e .

# Clean up test artifacts
clean:
	@echo "Cleaning up test artifacts..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
