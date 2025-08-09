# Testing for chemsource

This directory contains comprehensive tests for the chemsource package.

## Quick Test (Recommended for Installation Verification)

After installing the package, run a quick verification:

```bash
# Quick installation test
python tests/run_tests.py --quick

# Or using make
make test-quick
```

## Running All Tests

```bash
# Run all tests
python tests/run_tests.py

# Or using make
make test

# Or using unittest directly
python -m unittest discover tests -v
```

## API Provider Testing

### OpenAI API Testing
```bash
# Set environment variable and run tests
export OPENAI_API_KEY=your_openai_key
python tests/run_tests.py

# Or provide key inline
OPENAI_API_KEY=your_key python tests/run_tests.py
```

### Google Gemini API Testing
```bash
# Test Gemini integration specifically
export GEMINI_API_KEY=your_gemini_key
python tests/run_tests.py --gemini

# Or provide key inline
GEMINI_API_KEY=your_key python tests/run_tests.py --gemini
```

### Testing Without API Keys
```bash
# Run basic tests without API calls
python tests/run_tests.py --no-api-keys
```

## Test Types

### Integration Tests
Test that the package can be imported and basic functionality works:
```bash
python tests/run_tests.py --integration
```

### Unit Tests
Test individual components in isolation:
```bash
make test-unit
```

## Test Structure

- `test_config.py` - Tests for configuration management
- `test_exceptions.py` - Tests for custom exceptions
- `test_classifier.py` - Tests for AI classification functionality
- `test_retriever.py` - Tests for information retrieval
- `test_chemsource.py` - Tests for the main ChemSource class
- `test_integration.py` - Integration tests for package verification
- `run_tests.py` - Test runner with various options

### Test Runner Options

The `run_tests.py` script supports several options:

- `--quick` - Quick installation verification
- `--integration` - Run integration tests only
- `--gemini` - Test Google Gemini API integration specifically
- `--no-api-keys` - Skip API key checks (basic tests only)
- `--pattern` - Specify test file pattern (default: test_*.py)
- `--verbose` / `-v` - Increase verbosity

## Demo Script

Try the interactive demo to verify installation and test API providers:

```bash
# Basic demo (no API key required)
python examples/demo.py

# Demo with OpenAI API key (tests live functionality)
python examples/demo.py --with-api-key your_openai_api_key

# Demo with Google Gemini API key (tests Gemini integration)
python examples/demo.py --with-gemini-key your_gemini_api_key

# Offline mode (skip internet-dependent tests)
python examples/demo.py --offline-only
```

## Test Requirements

The tests use Python's built-in `unittest` framework and `unittest.mock` for mocking external dependencies. No additional test dependencies are required for basic testing.

Optional testing enhancements (install with `pip install -r requirements.txt`):
- `coverage` - For test coverage reports
- `pytest` - Alternative test runner
- `pytest-cov` - Coverage integration with pytest

## Development Workflow

1. **Install in development mode**: `pip install -e .`
2. **Run quick test**: `make test-quick`
3. **Run all tests**: `make test`
4. **Try the demo**: `python examples/demo.py`

## Continuous Integration

These tests are designed to work in CI environments and can run without external API keys by mocking the necessary dependencies.

## Test Coverage

The test suite covers:
- Package imports and basic setup
- Configuration management
- Exception handling
- Classification logic (mocked)
- Information retrieval (mocked)
- Main ChemSource class functionality
- Integration between components
- Multi-provider API support (OpenAI and Gemini)
- Custom client architecture

For live API testing, provide valid API keys to either the test runner or demo script.

## Multi-Provider Support

The chemsource package supports both OpenAI and Google Gemini APIs:

- **OpenAI**: Use `model_api_key` parameter or `OPENAI_API_KEY` environment variable
- **Gemini**: Use `custom_client` parameter with Gemini-configured OpenAI client

Both providers support all package features including clean output and category filtering.
