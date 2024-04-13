from config import Config
import engine

def configure(openai_key=None, model="gpt-4-0125-preview", ncbi_key=None, 
              prompt=Config.BASE_PROMPT, max_tokens=250000):
    Config().initialize(openai_key=openai_key, model=model, ncbi_key=ncbi_key, 
                        prompt=prompt, max_tokens=max_tokens)
#function that retrieves and classifies, 
#should return the info source, info text, classification, and description
def retcl(name):
    return engine.Drug(name).classify()

#only classify
def classify(name, information):
    return engine.Drug(name, information).classify()

#only retrieve info source and text
def retrieve(name):
    return engine.Drug(name).retrieve()

