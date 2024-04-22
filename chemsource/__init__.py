from config import Config
import engine

class ChemSource(Config, engine):
    def __init__(self, openai_key=None, model="gpt-4-0125-preview", ncbi_key=None, 
                 prompt=Config.BASE_PROMPT, max_tokens=250000):
        Config.__init__(self, openai_key=openai_key, model=model, ncbi_key=ncbi_key, 
                        prompt=prompt, max_tokens=max_tokens)
        