Installation
============

Requirements
============

chemsource requires Python 3.6 or later.

Install from PyPI
-----------------

.. code-block:: bash

    pip install chemsource

Install from Source
-------------------

.. code-block:: bash

    git clone https://github.com/prajitrr/chemsource.git
    cd chemsource
    pip install -e .

Dependencies
------------

chemsource depends on the following packages:

- ``lxml`` - For XML parsing
- ``openai`` - For AI model access
- ``pyspellchecker`` - For spell checking and correction
- ``requests`` - For HTTP requests
- ``wikipedia`` - For Wikipedia content retrieval

All dependencies will be installed automatically when you install chemsource.

Optional Dependencies
---------------------

For documentation generation:

- ``sphinx`` - Documentation generation
- ``sphinx-rtd-theme`` - Read the Docs theme
- ``sphinx-autodoc-typehints`` - Type hints support

.. code-block:: bash

    pip install sphinx sphinx-rtd-theme sphinx-autodoc-typehints
