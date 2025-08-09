# Makefile for chemsource testing and development

.PHONY: test test-quick test-integration test-unit test-gemini install-dev clean build docs help

# Default target
help:
	@echo "Available targets:"
	@echo "  test          - Run all tests"
	@echo "  test-quick    - Run quick installation verification"
	@echo "  test-integration - Run integration tests only"
	@echo "  test-unit     - Run unit tests only"
	@echo "  test-gemini   - Test Gemini API integration (requires GEMINI_API_KEY)"
	@echo "  install-dev   - Install package in development mode"
	@echo "  clean         - Clean up test artifacts"
	@echo "  build         - Build package for PyPI"
	@echo "  docs          - Build documentation with Sphinx"
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

# Test Gemini API integration
test-gemini:
	@echo "Testing Gemini API integration..."
	@echo "Note: Requires GEMINI_API_KEY environment variable"
	python tests/run_tests.py --gemini

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
	rm -rf build/ dist/ docs/_build/ 2>/dev/null || true

# Build package for PyPI
build: clean
	@echo "Building package for PyPI..."
	python -m build

# Build documentation with Sphinx
docs:
	@echo "Building documentation..."
	cd docs && make html
