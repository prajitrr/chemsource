Examples
========

This section provides detailed examples of using chemsource for various tasks.

Basic Classification
--------------------

.. code-block:: python

    from chemsource import ChemSource
    
    # Initialize with your API key
    chem = ChemSource(model_api_key="your_openai_api_key")
    
    # Classify a well-known medication
    info, classification = chem.chemsource("acetaminophen")
    print(f"Classification: {classification}")
    # Output: MEDICAL

Advanced Configuration
----------------------

.. code-block:: python

    from chemsource import ChemSource
    
    # Use custom configuration
    chem = ChemSource(
        model_api_key="your_openai_api_key",
        model="gpt-4o",
        clean_output=True,  # Enable output cleaning
        allowed_categories=["MEDICAL", "FOOD", "INDUSTRIAL", "PERSONAL CARE", "ENDOGENOUS", "INFO"]
    )
    
    # Classify with clean output
    info, classification = chem.chemsource("vitamin c")
    print(f"Clean classification: {classification}")
    # Output: ['ENDOGENOUS', 'FOOD']

Using Different Information Sources
-----------------------------------

.. code-block:: python

    from chemsource import ChemSource
    
    chem = ChemSource(
        model_api_key="your_openai_api_key",
        ncbi_key="your_ncbi_key"  # Optional for higher PubMed access rates
    )
    
    # Use Wikipedia as primary source (default)
    info1, class1 = chem.chemsource("caffeine", priority="WIKIPEDIA")
    
    # Use PubMed as primary source
    info2, class2 = chem.chemsource("caffeine", priority="PUBMED")
    
    # Use only one source
    info3, class3 = chem.chemsource("caffeine", priority="WIKIPEDIA", single_source=True)

Batch Processing
----------------

.. code-block:: python

    from chemsource import ChemSource
    
    chem = ChemSource(
        model_api_key="your_openai_api_key",
        clean_output=True,
        allowed_categories=["MEDICAL", "FOOD", "INDUSTRIAL", "PERSONAL CARE", "ENDOGENOUS", "INFO"]
    )
    
    compounds = ["aspirin", "glucose", "sodium chloride", "retinol", "benzene"]
    results = {}
    
    for compound in compounds:
        try:
            info, classification = chem.chemsource(compound)
            results[compound] = {
                'source': info[0],
                'classification': classification
            }
        except Exception as e:
            results[compound] = {'error': str(e)}
    
    # Print results
    for compound, result in results.items():
        if 'error' not in result:
            print(f"{compound}: {result['classification']} (from {result['source']})")
        else:
            print(f"{compound}: Error - {result['error']}")

Custom Client Usage
-------------------

.. code-block:: python

    from chemsource import ChemSource
    from openai import OpenAI
    
    # Create a custom OpenAI client with specific settings
    custom_client = OpenAI(
        api_key="your_openai_api_key",
        base_url="https://api.openai.com/v1",
        timeout=30.0
    )
    
    # Use the custom client
    chem = ChemSource(custom_client=custom_client)
    
    info, classification = chem.chemsource("morphine")
    print(f"Classification: {classification}")

Google Gemini Integration
-------------------------

.. code-block:: python

    from chemsource import ChemSource
    from openai import OpenAI
    
    # Create a custom client for Google Gemini API
    gemini_client = OpenAI(
        api_key="your_gemini_api_key",
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    
    # Use Gemini for classification
    chem = ChemSource(
        custom_client=gemini_client,
        model="gemini-2.5-flash"
    )
    
    info, classification = chem.chemsource("aspirin")
    print(f"Gemini classification: {classification}")
    
    # Use with clean output and category filtering
    chem_clean = ChemSource(
        custom_client=gemini_client,
        model="gemini-2.5-flash",
        clean_output=True,
        allowed_categories=["MEDICAL", "FOOD", "INDUSTRIAL", "PERSONAL CARE", "ENDOGENOUS", "INFO"]
    )
    
    info, clean_classification = chem_clean.chemsource("vitamin c")
    print(f"Clean classification: {clean_classification}")
    # Output: ['MEDICAL', 'FOOD']

Updating Configuration
----------------------

.. code-block:: python

    from chemsource import ChemSource
    
    chem = ChemSource()
    
    # Update configuration after initialization
    chem.configure(
        model_api_key="your_openai_api_key",
        model="gpt-4o",
        temperature=0.1,
        clean_output=True,
        allowed_categories=["MEDICAL", "FOOD"]
    )
    
    # Check current configuration
    config = chem.configuration()
    print(config)
    
    # Use individual setters
    chem.model("gpt-4.1")
    
    info, classification = chem.chemsource("insulin")

Using Explanation Feature
--------------------------

.. code-block:: python

    from chemsource import ChemSource
    
    # Create a custom prompt that includes explanation instructions
    custom_prompt = """You are a helpful scientist that will classify the provided compound 
    and explain your reasoning. First, provide a detailed explanation of your classification.
    Then write EXPLANATION_COMPLETE on a new line.
    Then provide only the categories as comma-separated values from: 
    MEDICAL, ENDOGENOUS, FOOD, PERSONAL CARE, INDUSTRIAL, INFO.
    
    Compound name: COMPOUND_NAME
    Information: """
    
    # Initialize with explanation feature enabled
    chem = ChemSource(
        model_api_key="your_openai_api_key",
        prompt=custom_prompt,
        clean_output=True,
        explanation=True,  # Enable explanation extraction
        explanation_separator="EXPLANATION_COMPLETE",  # Must match prompt
        allowed_categories=["MEDICAL", "FOOD", "INDUSTRIAL", "PERSONAL CARE", "ENDOGENOUS", "INFO"]
    )
    
    # The model will provide explanation + separator + classification
    # Only the classification part (after separator) will be returned
    info, classification = chem.chemsource("aspirin")
    print(f"Classification: {classification}")
    # Output: ['MEDICAL']
    
    # You can also use a custom separator
    custom_prompt_2 = """Explain your reasoning. Then write ### ANSWER ### 
    Then provide categories: COMPOUND_NAME Information: """
    
    chem_custom = ChemSource(
        model_api_key="your_openai_api_key",
        prompt=custom_prompt_2,
        clean_output=True,
        explanation=True,
        explanation_separator="### ANSWER ###",
        allowed_categories=["MEDICAL", "FOOD", "INDUSTRIAL"]
    )
```