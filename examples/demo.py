#!/usr/bin/env python3
"""
Demo script for chemsou        print("   ChemSource with custom configuration created successfully")
        
        # Verify some parameters
        assert chem_configured.model == "gpt-3.        except Exception as e:
            print(f"   Wikipedia retrieval failed: {e}")
        except Exception as e:
            print(f"   Unexpected error in retrieval: {e}")
            
    except Exception as e:
        print(f"   Error in offline retrieval test: {e}")
        return False
    
    return True       assert chem_configured.clean_output is False
        assert chem_configured.allowed_categories == ["MEDICAL", "ENDOGENOUS"]
        print("   Configuration parameters verified")
        
    except Exception as e:
        print(f"   Error in basic functionality: {e}")
        return False.

This script demonstrates basic usage of the chemsource package and can be used
to verify that the installation is working correctly.

Usage:
    python examples/demo.py [--with-api-key YOUR_OPENAI_KEY]
    
If no API key is provided, the script will only demonstrate offline functionality.
"""
import argparse
import sys
import os

# Add the src directory to the path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from chemsource import ChemSource
from chemsource.config import Config
from chemsource.exceptions import WikipediaRetrievalError


def demo_basic_functionality():
    """Demonstrate basic functionality without API calls."""
    print("="*60)
    print("CHEMSOURCE PACKAGE DEMO")
    print("="*60)
    
    print("\n1. Testing package import and basic setup...")
    try:
        # Test basic instantiation
        chem = ChemSource()
        print("   ChemSource imported and instantiated successfully")
        
        # Test configuration
        config = Config(
            model="gpt-4o-mini",
            clean_output=True,
            allowed_categories=["MEDICAL", "FOOD", "INDUSTRIAL"]
        )
        print("   Configuration object created successfully")
        
        # Test ChemSource with parameters
        chem_configured = ChemSource(
            model="gpt-3.5-turbo",
            clean_output=False,
            allowed_categories=["MEDICAL", "ENDOGENOUS"]
        )
        print("   ChemSource with custom configuration created successfully")
        
        # Verify configuration
        assert chem_configured.model == "gpt-3.5-turbo"
        assert chem_configured.clean_output is False
        assert chem_configured.allowed_categories == ["MEDICAL", "ENDOGENOUS"]
        print("   Configuration parameters verified")
        
    except Exception as e:
        print(f"   Error in basic functionality: {e}")
        return False
    
    print("\n2. Testing exception classes...")
    try:
        from chemsource.exceptions import (
            WikipediaRetrievalError,
            PubMedSearchXMLParseError
        )
        
        # Test exception instantiation
        wiki_error = WikipediaRetrievalError("Test error message")
        pubmed_error = PubMedSearchXMLParseError("Test XML parse error")
        
        print("   Exception classes imported and instantiated successfully")
        
    except Exception as e:
        print(f"   Error with exceptions: {e}")
        return False
    
    print("\n3. Testing module imports...")
    try:
        from chemsource.classifier import classify
        from chemsource.retriever import pubmed_retrieve, wikipedia_retrieve
        
        print("   Classifier and retriever modules imported successfully")
        
    except Exception as e:
        print(f"   Error importing modules: {e}")
        return False
    
    return True


def demo_with_api_key(api_key):
    """Demonstrate functionality with an actual API key."""
    print("\n4. Testing with API key (live functionality)...")
    
    try:
        # Create ChemSource with API key
        chem = ChemSource(model_api_key=api_key)
        print("   ChemSource created with API key")
        
        # Test a simple compound
        test_compound = "aspirin"
        print(f"   Testing with compound: {test_compound}")
        
        try:
            # Try to get information (this will make real API calls)
            info, classification = chem.chemsource(test_compound)
            
            print(f"   Successfully retrieved information for {test_compound}")
            print(f"   Classification: {classification}")
            
            if info[0]:  # Wikipedia info
                print(f"   Wikipedia info retrieved ({len(info[0])} characters)")
            if info[1]:  # PubMed info  
                print(f"   PubMed info retrieved ({len(info[1])} characters)")
                
        except Exception as e:
            print(f"   API call failed (this might be expected): {e}")
            
    except Exception as e:
        print(f"   Error with API functionality: {e}")
        return False
    
    return True


def demo_with_gemini_api(api_key):
    """Demonstrate functionality with Google Gemini API."""
    print("\n4. Testing with Gemini API key (live functionality)...")
    
    try:
        from openai import OpenAI
        
        # Create custom client for Gemini
        custom_client = OpenAI(
            api_key=api_key,
            base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
        )
        
        chem = ChemSource(
            custom_client=custom_client,
            model='gemini-2.5-flash'
        )
        print("   ChemSource created with Gemini API")
        
        # Test basic functionality
        test_compound = "caffeine"
        print(f"   Testing with compound: {test_compound}")
        
        try:
            info, classification = chem.chemsource(test_compound)
            
            print(f"   Successfully retrieved information for {test_compound}")
            print(f"   Classification: {classification}")
            
            if info[0]:  # Source
                print(f"   Information source: {info[0]}")
            if info[1]:  # Content
                print(f"   Content retrieved ({len(info[1])} characters)")
                
        except Exception as e:
            print(f"   Gemini API call failed: {e}")
            return False
            
        # Test clean output functionality
        print("   Testing clean output with Gemini...")
        try:
            chem_clean = ChemSource(
                custom_client=custom_client,
                model='gemini-2.5-flash',
                clean_output=True,
                allowed_categories=['MEDICAL', 'FOOD', 'INDUSTRIAL', 'PERSONAL CARE', 'ENDOGENOUS']
            )
            
            info, classification = chem_clean.chemsource("vitamin c")
            print(f"   Clean output classification: {classification}")
            
        except Exception as e:
            print(f"   Clean output test failed: {e}")
            
    except Exception as e:
        print(f"   Error with Gemini API functionality: {e}")
        return False
    
    return True


def demo_offline_retrieval():
    """Demonstrate retrieval functionality that doesn't require OpenAI API."""
    print("\n5. Testing offline retrieval capabilities...")
    
    try:
        chem = ChemSource()  # No API key needed for retrieval only
        
        # Test Wikipedia retrieval (doesn't need OpenAI API)
        test_compound = "caffeine"
        print(f"   Testing Wikipedia retrieval for: {test_compound}")
        
        try:
            info = chem.retrieve(test_compound, priority="WIKIPEDIA")
            if info[0]:  # Wikipedia content
                print(f"   Wikipedia retrieval successful ({len(info[0])} characters)")
            else:
                print("   No Wikipedia content retrieved")
                
        except WikipediaRetrievalError as e:
            print(f"   ⚠️  Wikipedia retrieval failed: {e}")
        except Exception as e:
            print(f"   Unexpected error in retrieval: {e}")
            
    except Exception as e:
        print(f"   Error in offline retrieval test: {e}")
        return False
    
    return True


def main():
    """Main demo function."""
    parser = argparse.ArgumentParser(description='Demo script for chemsource package')
    parser.add_argument('--with-api-key', 
                       help='OpenAI API key for testing live functionality')
    parser.add_argument('--with-gemini-key',
                       help='Google Gemini API key for testing Gemini integration')
    parser.add_argument('--offline-only', action='store_true',
                       help='Skip tests that require internet connection')
    
    args = parser.parse_args()
    
    print("Starting chemsource package demonstration...")
    
    # Test basic functionality
    success = demo_basic_functionality()
    
    if not success:
        print("\nBasic functionality test failed")
        print("Please check your installation with: pip install -e .")
        sys.exit(1)
    
    # Test offline retrieval if not in offline-only mode
    if not args.offline_only:
        success &= demo_offline_retrieval()
    
    # Test with OpenAI API key if provided
    if args.with_api_key:
        success &= demo_with_api_key(args.with_api_key)
    elif args.with_gemini_key:
        success &= demo_with_gemini_api(args.with_gemini_key)
    else:
        print("\n   Skipping live API tests (no API key provided)")
        print("     Use --with-api-key YOUR_OPENAI_KEY to test OpenAI functionality")
        print("     Use --with-gemini-key YOUR_GEMINI_KEY to test Gemini functionality")
    
    print("\n" + "="*60)
    if success:
        print("Demo completed successfully.")
        print("\nThe chemsource package is ready to use.")
        print("\nNext steps:")
        print("1. Get an API key:")
        print("   - OpenAI: https://platform.openai.com/")
        print("   - Google Gemini: https://aistudio.google.com/")
        print("2. For OpenAI: chem = ChemSource(model_api_key='your_key')")
        print("3. For Gemini: chem = ChemSource(custom_client=gemini_client)")
        print("4. Try: info, classification = chem.chemsource('aspirin')")
    else:
        print("Demo encountered issues.")
        print("\nPlease check your installation and try again.")
        print("For help, see: https://chemsource.readthedocs.io/")
    
    print("="*60)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
