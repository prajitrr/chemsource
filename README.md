# chemsource v1.0.3
`chemsource` is a tool for exposomics research that classifies chemicals based on their exposure sources. The tool is currently offered in Python. The current iteration, `v1.0.3`, first retrieves information from [Wikipedia](https://www.wikipedia.org/) and the [PubMed](https://pubmed.ncbi.nlm.nih.gov/) abstract database. Information retrieved is then used to classify chemicals based on their exposure sources using OpenAI's [ChatGPT API](https://platform.openai.com/docs/api-reference) into a combination of 5 categories, `MEDICAL, ENDOGENOUS, FOOD, PERSONAL CARE,` or `INDUSTRIAL`. Chemicals without enough available information will be classified with the tag `INFO`.

## Installation & Setup
`chemsource` is available on `pypi` [here](https://pypi.org/project/chemsource/) or can alternatively be downloaded directly from the [GitHub repository](https://github.com/prajitrr/chemsource). 

To install directly from `pypi`, make sure you have `pip` installed on your system, which can be found [here](https://pypi.org/project/pip/). Then, you can run the following command in a terminal shell.

```
pip install chemsource
```

To use the classification feature of `chemsource`, users must have an OpenAI API key that can be provided to the model along with credits associated with the key. Information on where to find the key can be found [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key). Credits can be added to your OpenAI account [here](https://platform.openai.com/account/billing/overview). Note that new users of the OpenAI API receive $5.00 in free credits, which is a sufficient amount to use `chemsource` for the purposes of small-scale testing. See `Cost` for more information.

## Usage

### Import and Configuration
Import the package using the following command:
```
from chemsource import ChemSource()
```
A `chemsource` model can be configured by calling the constructor `ChemSource()`. Models have various parameters that can be changed to suit user needs.
```
model = ChemSource() 
```
View the model's current parameters using `configuration()`
```
model.configuration()
```
The output is a dictionary of parameters. The default parameters are displayed here.
```
{'openai_key': None,
 'ncbi_key': None,
 'model': 'gpt-4-0125-preview',
 'prompt': 'Classify this compound, COMPOUND_NAME, as any combination of the following: MEDICAL, ENDOGENOUS, FOOD, PERSONAL CARE, INDUSTRIAL. Note that ENDOGENOUS refers to compounds that are human synthesized. ENDOGENOUS excludes essential nutrients that cannot be synthesized by the human body. Note that FOOD refers to compounds present in natural food items. Note that INDUSTRIAL should be used only for compounds not used as a contributing ingredient in the medical, personal care, or food industries. Note that PERSONAL CARE refers to non-medicated compounds typically used for activities such as skincare, beauty, and fitness. Specify INFO instead if more information is needed. DO NOT MAKE ANY ASSUMPTIONS, USE ONLY THE INFORMATION PROVIDED. Provide the output as a plain text separated by commas, and provide only the categories listed (either list a combination of INDUSTRIAL, ENDOGENOUS, PERSONAL CARE, MEDICAL, FOOD or list INFO), with no justification. Provided Information:\n',
 'token_limit': 250000}
```
`openai_key` is the API key from OpenAI necessary for classification. However, information retrieval can still be performed without a configured `openai_key`.

`ncbi_key` is an NCBI API Key used for information retrieval from PubMed but is not required. Information retrieval without an NCBI API Key is limited to 3 requests to PubMed per second, while retrieval with the API Key is limited to 10 requests to PubMed per second. For prolonged use for classification of large numbers of compounds, it is recommended to obtain an NCBI API Key and provide it to the model. Information on how to obtain an NCBI API Key can be found [here](https://support.nlm.nih.gov/knowledgebase/article/KA-05317/en-us). The API Key is free to anyone.

`model` is the OpenAI model that is used for classification. The default model, `gpt-4-0125-preview`, was found to perform best for the classification task. A list of models and their properties can be found on the OpenAI [website](https://platform.openai.com/docs/models). Note that different models have differing prices. More information on this can be found in the [Cost](https://github.com/prajitrr/chemsource?tab=readme-ov-file#cost) section of the documentation.

`prompt` is the base prompt fed to the OpenAI model that informs the model of the classification task. The default prompt is optimized for the default classifications but may be tweaked or changed as desired for differential mining of the information retrieved. Within each prompt, use the String `COMPOUND_NAME` to indicate the location in the prompt in which the name of the chemical being queried should be placed.

`token_limit` is a limit on the length of each query sent to OpenAI, in tokens, designed to place a limit on the cost per query of the model. Any text beyond `token_limit` is truncated. For more information, see the next section, [Cost](https://github.com/prajitrr/chemsource?tab=readme-ov-file#cost).

### Classification

#### Basic Usage & Default Classification
The main classification function can be called using `chemsource()` and requires a single parameter, the name of the chemical or drug to be classified. An example classification on the drug `"melatonin"` is shown below.
```
# Configure a model with an OpenAI API Key, which can be used for multiple classifications
user_openai_key = "" # Insert your OpenAI API Key here
model = chemsource.ChemSource(openai_key=user_openai_key) 

# Call chemsource() using the desired chemical as an input
result = model.chemsource("melatonin")
```
The output, `result`, is a tuple. `result[0]` is itself a tuple with the first entry being the source of the result, `"WIKIPEDIA"` or `"PUBMED"`. The second entry in `result[0]` is the text used for classification. `result[1]` provides the actual output of the classifcation task, a comma-separated plain text list of categories that fit the chemical queried.

Calling `result[0]` for `"melatonin"` results in the following (note that the output is truncated here):
```
("WIKIPEDIA",
 "Melatonin, an indoleamine, is a natural compound produced by various organisms, including bacteria and eukaryotes. Its discovery in 1958 by Aaron B. Lerner and colleagues stemmed from the isolation of a substance from the pineal gland of cows that could induce skin lightening in common frogs. This compound was later identified as a hormone secreted in the brain during the night, playing a cruc...")
```

Calling `result[1]` for `"melatonin"` results in the following classification:
```
"ENDOGENOUS, MEDICAL, FOOD"
```
#### Source Control
The `chemsource()` function also has two additional optional arguments, `priority`, and `single_source`. 

`priority` has two options, `"WIKIPEDIA"` or `"PUBMED"`, and it determines which source is checked first for information. The default option is `priority="WIKIPEDIA"` as Wikipedia is generally more comprehensive. 

`single_source` is a boolean value, with the default option being `single_source=False`. If set to `True`, the model will only obtain information from the prioritized source set by `priority` and will not consider the other source, even if no information is retrieved.

#### Information Retrieval Only 
In addition to the main `chemsource()` function, the package also provides two other functions, `retrieve()` and `classify()`. Both are called as methods of a `ChemSource()` object.

`retrieve()` is used to retrieve the text used by the model for classification and takes in a single required parameter, the drug name, in addition to two optional parameters, `priority`, and `single_source`, which serve the same purpose as in the `chemsource()` function. 

An example of `retrieve()` using `"melatonin"` and the model declared in the steps above:
```
retrieval_result_1 = model.retrieve("melatonin") #Without changing the default parameters

retrieval_result_2 = model.retrieve("melatonin", priority="PUBMED", single_source=True) #Default parameters changed
```

The output is a tuple in which the first entry is the source and the second entry is the text retrieved. Note that `retrieve()` does not require an OpenAI API Key to be inputted into the model configuration.

The results derived from calling the retrieval functions as shown above (note that the output is truncated here).

`retrieval_result_1[0]`
```
"WIKIPEDIA"
```

`retrieval_result_1[1]`
```
"Melatonin, an indoleamine, is a natural compound produced by various organisms, including bacteria and eukaryotes. Its discovery in 1958 by Aaron B. Lerner and colleagues stemmed from the isolation of a substance from the pineal gland of cows that could induce skin lightening in common frogs. This compound was later identified as a hormone secreted in the brain during the night, playing a cruc..."
```

`retrieval_result_2[0]`
```
"PUBMED"
```

`retrieval_result_2[1]`
```
"Melatonin is the main hormone involved in the control of the sleep-wake cycle. It is easily synthesisable and can be administered orally, which has led to interest in its use as a treatment for insomnia. Moreover, as production of the hormone decreases with age, in inverse correlation with the frequency of poor sleep quality, it has been suggested that melatonin deficit is at least partly resp..."
```

#### Classification Only
`classify()` is used to classify a chemical given a pre-existing text, with two required inputs, the first being the chemical that the text refers to and the second being the text itself.

An example of `classify()` using `"melatonin"` and its associated text derived from Wikipedia (note that the input is truncated here).
```
classification_result = model.classify("melatonin", "Melatonin, an indoleamine, is a natural compound produced by various organisms, including bacteria and eukaryotes. Its discovery in 1958 by Aaron B. Lerner and colleagues stemmed from the isolation of a substance from the pineal gland of cows that could induce skin lightening in common frogs. This compound was later identified as a hormone secreted in the brain during the night, playing a cruc...")
```

The output is a plain-text list of categories that is separated by commas, similar to the `chemsource()` function. The output of the previous example of `classify()` using `"melatonin"` is shown below.
`classification_result`
```
"ENDOGENOUS, MEDICAL, FOOD"
```

When running the model on a large number of chemicals, it may be more feasible to first run `retrieve()` on the list of chemicals, store the information, and then run `classify()` on the result to avoid having to perform a single excessively long run.

Classification tasks can easily be run in large batches using simple default Python loops or library functions such as `apply()` from `pandas`.

#### Customized Classification by Prompt Editing
As previously described, the `prompt` property of a `chemsource` model can be modified for other tasks. Below, an example of a different classification task is shown.

```
# Configure a model with an OpenAI API Key and a modified prompt
user_openai_key = "" # Insert your OpenAI API Key here
modified_prompt = "Classify this compound, COMPOUND_NAME, based on the ICD-10 chapter of the disease or disorder it is used to treat. ICD-10 chapters are labeled using Roman numerals, and a list of ICD-10 chapters and their descriptions is as follows: I: Certain infectious and parasitic diseases, II: Neoplasms, III: Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism, IV: Endocrine, nutritional and metabolic diseases, V: Mental and behavioural disorders, VI: Diseases of the nervous system, VII: Diseases of the eye and adnexa, VIII: Diseases of the ear and mastoid process, IX: Diseases of the circulatory system, X: Diseases of the respiratory system, XI: Diseases of the digestive system, XII: Diseases of the skin and subcutaneous tissue, XIII: Diseases of the musculoskeletal system and connective tissue, XIV: Diseases of the genitourinary system, XV: Pregnancy, childbirth and the puerperium, XVI: Certain conditions originating in the perinatal period, XVII: Congenital malformations, deformations and chromosomal abnormalities, XVIII: Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified, XIX: Injury, poisoning and certain other consequences of external causes, XX: External causes of morbidity and mortality, XXI: Factors influencing health status and contact with health services, XXII: Codes for special purposes. Apply a classification using any combination of the Roman numerals listed above. Specify INFO instead if more information is needed. DO NOT MAKE ANY ASSUMPTIONS, USE ONLY THE INFORMATION PROVIDED. Provide the output as a plain text separated by commas, and provide only the Roman numerals listed above or INFO, with no justification. Provided Information:\n"

modified_model = chemsource.ChemSource(openai_key=user_openai_key, prompt=modified_prompt) 

# Call chemsource() using the modified model and the desired chemical as an input
result = model.chemsource("melatonin")
```

The output, `result`, remains in the same format as the unmodified model. Below is the value stored in `result[1]`, which contains the output of the new task.

```
"V"
```

This is the ICD-10 chapter for mental and behavioural disorders, showing that the model was successful with the newly defined classification task. Tasks are not limited to classification only and can also include commands such as summarizing, making predictions, and much more. 

## Cost
`chemsource` as a package is available with no additional charge to all users. However, the use of OpenAI's ChatGPT models within the classification step of the package is a service that costs money due to the energetically demanding nature of Large Language Models. The price is determined based on the number of tokens in the input, a measure of the length of text inputted into the model. Information on the current price of each ChatGPT model can be found on the OpenAI [website](https://openai.com/pricing). A second version of `chemsource` that does not incur API charges is currently in development.