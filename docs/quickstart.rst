Quick Start
===========

This guide will help you get started with chemsource quickly.

Basic Usage
-----------

.. code-block:: python

    from chemsource import ChemSource
    
    # Initialize ChemSource with your OpenAI API key
    chem = ChemSource(model_api_key="your_openai_api_key")
    
    # Retrieve information and classify a compound
    info, classification = chem.chemsource("aspirin")
    
    print(f"Source: {info[0]}")
    print(f"Content: {info[1][:100]}...")
    print(f"Classification: {classification}")

Configuration
-------------

You can configure chemsource with various parameters:

.. code-block:: python

    from chemsource import ChemSource
    
    # Configure with custom settings
    chem = ChemSource(
        model_api_key="your_openai_api_key",
        model="gpt-4-0125-preview",
        temperature=0.1,
        clean_output=True,
        allowed_categories=["MEDICAL", "FOOD", "INDUSTRIAL", "PERSONAL CARE", "ENDOGENOUS"]
    )

Retrieving Information Only
---------------------------

If you only want to retrieve information without classification:

.. code-block:: python

    from chemsource import ChemSource
    
    chem = ChemSource()
    
    # Retrieve from Wikipedia (default)
    source, content = chem.retrieve("caffeine")
    
    # Retrieve from PubMed (requires NCBI key)
    chem.ncbi_key = "your_ncbi_key"
    source, content = chem.retrieve("caffeine", priority="PUBMED")

Classification Only
-------------------

If you already have information about a compound:

.. code-block:: python

    from chemsource import ChemSource
    
    chem = ChemSource(model_api_key="your_openai_api_key")
    
    compound_info = "Aspirin is a medication used to reduce pain, fever, or inflammation."
    classification = chem.classify("aspirin", compound_info)
    
    print(classification)

Using Clean Output
------------------

For structured output with spell checking and validation:

.. code-block:: python

    from chemsource import ChemSource
    
    chem = ChemSource(
        model_api_key="your_openai_api_key",
        clean_output=True,
        allowed_categories=["MEDICAL", "FOOD", "INDUSTRIAL", "PERSONAL CARE", "ENDOGENOUS"]
    )
    
    info, classification = chem.chemsource("ibuprofen")
    
    # classification will be a list of validated categories
    print(classification)  # ['MEDICAL']
