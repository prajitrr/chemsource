from src.chemsource.config import Config
from engine import classifier
from engine import retriever

class ChemSource(Config):
    def __init__(self, 
                 openai_key=None, 
                 model="gpt-4-0125-preview", 
                 ncbi_key=None, 
                 prompt=Config.BASE_PROMPT, 
                 max_tokens=250000
                 ):
        super().__init__(self, 
                         openai_key=openai_key, 
                         model=model, 
                         ncbi_key=ncbi_key,
                         prompt=prompt, 
                         max_tokens=max_tokens
                         )
    
    def chemsource(self, name, priority="WIKIPEDIA", single_source=False):
        if self.openaikey is None:
            raise ValueError("OpenAI API key must be provided")

        information = retriever.retrieve(name, 
                                         priority,
                                         single_source, 
                                         ncbikey=self.ncbi_key
                                         )
        
        return information, classifier.classify(name, 
                                                information, 
                                                self.openai_key,
                                                self.prompt,
                                                self.model,
                                                self.max_tokens)

    def classify(self, name, information):
        if self.openaikey is None:
            raise ValueError("OpenAI API key must be provided")
        
        return classifier.classify(name, 
                                   information,
                                   self.openai_key,
                                   self.prompt,
                                   self.model,
                                   self.max_tokens)
    
    def retrieve(self, name, priority="WIKIPEDIA", single_source=False):
        return retriever.retrieve(name, 
                                  priority, 
                                  single_source,
                                  ncbikey=self.ncbi_key
                                  )