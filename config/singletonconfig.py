BASE_PROMPT = ("Classify this compound, COMPOUND_NAME, as any combination of" 
               + " the following: MEDICAL, ENDOGENOUS, FOOD, PERSONAL CARE,"
               + " INDUSTRIAL. Note that ENDOGENOUS refers to compounds that" 
               + " are human synthesized. ENDOGENOUS excludes essential" 
               + " nutrients that cannot be synthesized by human body. Note"
               + " that FOOD refers to compounds present in natural food" 
               + " items. Note that INDUSTRIAL should be used only for" 
               + " compounds not used as a contributing ingredient in the" 
               + " medical, personal care, or food industries. Note that" 
               + " PERSONAL CARE refers to non-medicated compounds typically" 
               + " used for activities such as skincare, beauty, and fitness." 
               + " Specify INFO instead if more information is needed. DO NOT" 
               + " MAKE ANY ASSUMPTIONS, USE ONLY THE INFORMATION PROVIDED." 
               + " Provide the output as a plain text separated by commas," 
               + " and provide only the categories listed (either list a" 
               + "combination of INDUSTRIAL, ENDOGENOUS, PERSONAL CARE," 
               + " MEDICAL, FOOD or list INFO), with no justification." 
               + " Provided Information:\n")

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def initialize(self, openai_key=None, model="gpt-4-0125-preview", 
                   ncbi_key=None, prompt=BASE_PROMPT, max_tokens=250000):
        if not self._initialized:
            self.openai_key = openai_key
            self.model = model
            self.ncbi_key = ncbi_key
            self.prompt = prompt
            self.max_tokens = max_tokens
            self._initialized = True

    def configure(self, )
        
    @classmethod

