from openai import OpenAI 

class Drug(object):
  def __init__(self, name, description = None, info_source=None, classification=None):
    self.name = name
    self.description = description #or ""
    self.info_source = info_source #or ""
    self.classification = classification #or []
  
  def __str__(self):
    return self.name
  
  def description(self):
    return self.description
  
  def info_source(self):
    return self.info_source
  
  def classification(self):
    return self.classification
  
  from ._retriever import retrieve
    
  def classify(self):
    return self.classification
    
  def chemsource(self, name):
    