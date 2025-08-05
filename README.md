# chemsource

[![Documentation Status](https://readthedocs.org/projects/chemsource/badge/?version=latest)](https://chemsource.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/chemsource.svg)](https://badge.fury.io/py/chemsource)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

chemsource is a Python tool for exposomics research that classifies chemical compounds based on their exposure sources. It retrieves information from Wikipedia and PubMed, then uses large language models to classify chemicals into categories such as MEDICAL, ENDOGENOUS, FOOD, PERSONAL CARE, and INDUSTRIAL.


## Quick Start

```python
from chemsource import ChemSource

# Initialize with your OpenAI API key
chem = ChemSource(model_api_key="your_openai_api_key")

# Classify a compound
info, classification = chem.chemsource("aspirin")
print(f"Classification: {classification}")
```

## Installation

Install from PyPI:

```bash
pip install chemsource
```

## Documentation

For detailed documentation, tutorials, and API reference, visit:

**[📖 Read the Docs](https://chemsource.readthedocs.io/)**

The documentation includes:
- Installation and setup instructions
- Comprehensive API reference
- Usage examples and tutorials
- Configuration options
- Error handling guides

## Requirements

- Python 3.6+
- OpenAI (or other LLM) API key (for classification)
- NCBI API key (optional, for enhanced PubMed access)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use ChemSource in your research, please cite:
(Preprint coming soon)

```
```

## Support

- 📚 [Documentation](https://chemsource.readthedocs.io/)
- 🐛 [Issue Tracker](https://github.com/prajitrr/chemsource/issues)
- 📧 [Contact](mailto:prajkumar@ucsd.edu)

---

**Note**: ChemSource uses OpenAI's API services which incur costs based on usage. New users receive $5 in free credits, sufficient for testing purposes.