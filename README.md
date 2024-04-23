# chemsource v1.0.2
`chemsource` is a tool to classify novel drugs and other chemicals by source that is currently offered in Python. The current iteration, `v1.0.2`, relies on information scraped from [Wikipedia](https://www.wikipedia.org/) and the NLM's [PubMed](https://pubmed.ncbi.nlm.nih.gov/) abstract database. Information retrieved is classified using OpenAI's [ChatGPT API](https://platform.openai.com/docs/api-reference) into a combination of 5 categories, `MEDICAL, ENDOGENOUS, FOOD, PERSONAL CARE,` or `INDUSTRIAL`. Chemicals without enough available information will be classified with the tag `INFO`.

## Installation & Setup
`chemsource` is available on `pypi` [here](https://pypi.org/project/chemsource/) or can alternatively be downloaded directly from the [GitHub repository](https://github.com/prajitrr/chemsource). 

To install directly from `pypi`, make sure you have `pip` installed on your system, which can be found [here](https://pypi.org/project/pip/). Then, you can run the following command in a terminal shell.

```
pip install chemsource
```

To use the classification feature of `chemsource`, users must have an OpenAI API key that can be provided to the model along with credits associated with the key. Information on where to find the key can be found [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key). Credits can be added to your OpenAI account [here](https://platform.openai.com/account/billing/overview). Note that new users of the OpenAI API receive $5.00 in free credits, which should be a sufficient amount to use `chemsource` for the purposes of small-scale testing. See `Cost` for more information.

## Usage


## Cost
`chemsource` as a package is available with no additional charge to all users. However, the use of OpenAI's ChatGPT models within the classification step of the package is a service that costs money due to the energetically demanding nature of Large Language Models. Information on the current price of each ChatGPT model can be found on the OpenAI [website](https://openai.com/pricing)