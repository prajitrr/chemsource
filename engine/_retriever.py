#!pip install wikipedia
#IMPORTANT IN FINAL VERSION, FIGURE OUT HOW TO EITHER QUERY WITHOUT
#PUBMED KEY OR HOW TO GET A PUBMED KEY FROM USER

from exceptions import XMLParseError, XMLRetrievalError
from exceptions import XMLParseError2, XMLRetrievalError2, JoinError

from lxml import etree
import re
import requests as r
import wikipedia

SEARCH_PARAMS = {'db': 'pubmed',
                 'term': '',
                 'retmax': '3',
                 'usehistory': 'n',
                 'sort': 'relevance',
                 'api_key': 'bdd2f83e20dc27d1e257d3896d036fd0a108'
                 }

XML_RETRIEVAL_PARAMS = {'db': 'pubmed',
                        'query_key': '1',
                        'WebEnv': '',
                        'rettype': 'abstract',
                        'retmax': '3',
                        'api_key': 'bdd2f83e20dc27d1e257d3896d036fd0a108'
                        }

def retrieve(self, name)
    
def pubmed_retrieve(drug):
    SEARCH_PARAMS['term'] = drug + '[ti]'
    try:
        xml_content = etree.fromstring(r.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?", params=SEARCH_PARAMS).content)
    except:
        raise XMLParseError
    try:
        if (str(xml_content.find(".//Count").text) == 0):
            return 'NO_RESULTS'
    except:
        raise XMLRetrievalError
    else:
        XML_RETRIEVAL_PARAMS['WebEnv'] = xml_content.find(".//WebEnv").text
        try:
            retrieval_content = etree.fromstring(r.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?', params=XML_RETRIEVAL_PARAMS).content)
        except:
            raise XMLParseError2
        try:
            abstracts = retrieval_content.findall(".//AbstractText")
        except:
            raise XMLRetrievalError2
        result = ''
        try:
            for abstract in abstracts:
                result = result + ' ' + abstract.text
        except:
            raise JoinError
        return result

def wikipedia_retrieve(drug):
    description = wikipedia.page(drug, auto_suggest=False).content
    description = description.replace('\n', ' ')
    description = description.replace('\t', ' ')
    description = ' '.join(description.split())
    return description