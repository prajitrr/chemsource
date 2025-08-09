#!/usr/bin/env python3
"""
Test runner for chemsource package.
This script runs all tests and provides a summary of results.
"""
import sys
import os
import unittest
import argparse
from io import StringIO

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def check_api_keys():
    """
    Check if required API keys are available for testing.
    Returns tuple of (openai_key, ncbi_key, gemini_key) or raises ValueError if missing.
    """
    openai_key = os.environ.get('OPENAI_API_KEY')
    ncbi_key = os.environ.get('NCBI_API_KEY')  # Optional
    gemini_key = os.environ.get('GEMINI_API_KEY')  # Optional
    
    if not openai_key and not gemini_key:
        raise ValueError(
            "Either OPENAI_API_KEY or GEMINI_API_KEY environment variable is required for running tests. "
            "Please set one with: export OPENAI_API_KEY=your_key_here or export GEMINI_API_KEY=your_key_here"
        )
    
    return openai_key, ncbi_key, gemini_key


def run_tests(test_pattern='test_*.py', verbosity=2, integration_only=False, require_api_keys=True):
    """
    Run tests with the specified pattern and verbosity.
    
    Args:
        test_pattern (str): Pattern for test files to run
        verbosity (int): Verbosity level (0, 1, or 2)
        integration_only (bool): If True, only run integration tests
        require_api_keys (bool): If True, check for API keys before running tests
    
    Returns:
        bool: True if all tests passed, False otherwise
    """
        # Check for API keys if required
    if require_api_keys and not integration_only:
        try:
            openai_key, ncbi_key, gemini_key = check_api_keys()
            if openai_key:
                print(f"OpenAI API key found")
            if gemini_key:
                print(f"Gemini API key found")
            if ncbi_key:
                print(f"NCBI API key found")
        except ValueError as e:
            print(f"API key check failed: {e}")
            return False
    
    # Discover and run tests
    test_dir = os.path.dirname(__file__)
    
    if integration_only:
        # Only run integration tests
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName('test_integration', test_dir)
    else:
        # Discover all tests
        loader = unittest.TestLoader()
        suite = loader.discover(test_dir, pattern=test_pattern)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=verbosity, stream=sys.stdout)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped) if hasattr(result, 'skipped') else 0}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback.split('AssertionError:')[-1].strip()}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            error_lines = traceback.split('\n')
            error_msg = error_lines[-2].strip() if len(error_lines) > 1 else str(traceback).strip()
            print(f"- {test}: {error_msg}")
    
    success = len(result.failures) == 0 and len(result.errors) == 0
    print(f"\nResult: {'PASSED' if success else 'FAILED'}")
    print("="*50)
    
    return success


def test_gemini_integration():
    """
    Test Gemini API integration specifically.
    This is useful for verifying custom_client functionality.
    """
    print("Testing Gemini API integration...")
    print("-" * 40)
    
    try:
        gemini_key = os.environ.get('GEMINI_API_KEY')
        if not gemini_key:
            print("Gemini API key not found. Set GEMINI_API_KEY to test Gemini integration.")
            return False
        
        print("Testing Gemini imports...")
        from openai import OpenAI
        from chemsource import ChemSource
        
        print("Creating Gemini client...")
        custom_client = OpenAI(
            api_key=gemini_key,
            base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
        )
        
        print("Testing basic Gemini classification...")
        chem = ChemSource(
            custom_client=custom_client,
            model='gemini-2.5-flash'
        )
        
        # Test simple classification
        info, classification = chem.chemsource('aspirin')
        print(f"Basic classification successful: {classification}")
        
        print("Testing clean output with Gemini...")
        chem_clean = ChemSource(
            custom_client=custom_client,
            model='gemini-2.5-flash',
            clean_output=True,
            allowed_categories=['MEDICAL', 'FOOD', 'INDUSTRIAL', 'PERSONAL CARE', 'ENDOGENOUS', 'INFO']
        )
        
        info, classification = chem_clean.chemsource('caffeine')
        print(f"Clean output classification successful: {classification}")
        
        print("\nGemini integration test completed successfully.")
        return True
        
    except Exception as e:
        print(f"\nGemini integration test failed: {e}")
        return False


def quick_test():
    """
    Run a quick test to verify the package is properly installed.
    This is useful for post-installation verification.
    """
    print("Running quick installation verification...")
    print("-" * 40)
    
    try:
        # Test basic imports
        print("Testing package imports...")
        import chemsource
        from chemsource import ChemSource
        from chemsource.config import Config
        from chemsource.exceptions import WikipediaRetrievalError
        
        # Test basic instantiation
        print("Testing basic instantiation...")
        config = Config()
        chem = ChemSource()
        
        # Test that configuration works
        print("Testing configuration...")
        chem_configured = ChemSource(
            model="gpt-4o-mini",
            clean_output=True,
            allowed_categories=["MEDICAL", "FOOD"]
        )
        
        assert chem_configured.model == "gpt-4o-mini"
        assert chem_configured.clean_output is True
        assert chem_configured.allowed_categories == ["MEDICAL", "FOOD"]
        
        print("Testing dependencies...")
        import openai
        import requests
        import lxml
        import wikipedia
        from spellchecker import SpellChecker
        
        print("\nAll quick tests passed. Package is ready to use.")
        print("\nTo run full tests, use: python -m tests.run_tests")
        return True
        
    except Exception as e:
        print(f"\nQuick test failed: {e}")
        print("\nTry installing the package with: pip install -e .")
        return False


def main():
    """Main function to handle command line arguments and run tests."""
    parser = argparse.ArgumentParser(description='Run tests for chemsource package')
    parser.add_argument('--quick', action='store_true', 
                       help='Run quick installation verification only')
    parser.add_argument('--integration', action='store_true',
                       help='Run integration tests only')
    parser.add_argument('--gemini', action='store_true',
                       help='Test Gemini API integration specifically')
    parser.add_argument('--pattern', default='test_*.py',
                       help='Pattern for test files (default: test_*.py)')
    parser.add_argument('--verbose', '-v', action='count', default=1,
                       help='Increase verbosity (use -vv for max verbosity)')
    parser.add_argument('--no-api-keys', action='store_true',
                       help='Skip API key checks (for basic tests only)')
    
    args = parser.parse_args()
    
    if args.quick:
        success = quick_test()
        sys.exit(0 if success else 1)
    
    if args.gemini:
        success = test_gemini_integration()
        sys.exit(0 if success else 1)
    
    # Determine verbosity level
    verbosity = min(args.verbose, 2)
    
    print(f"Running chemsource tests...")
    print(f"Pattern: {args.pattern}")
    print(f"Verbosity: {verbosity}")
    if args.integration:
        print("Mode: Integration tests only")
    elif args.no_api_keys:
        print("Mode: Basic tests only (no API calls)")
    print("-" * 40)
    
    success = run_tests(
        test_pattern=args.pattern,
        verbosity=verbosity,
        integration_only=args.integration,
        require_api_keys=not args.no_api_keys
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
