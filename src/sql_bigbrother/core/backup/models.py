from langchain_community import Ollama

class Models():
    def llama3_8b(self):
        return Ollama(model="llama3-8b")
    
    def llama3_70b(self):
        return Ollama(model="llama3-70b")

    def gemma2_9b(self):
        return Ollama(model="gemma2")
    
    def mistral_7b(self):
        return Ollama(model="mistral")

    def phi3_mini(self):
        return Ollama(model="phi3-mini")
    
    def phi3_medium(self):
        return Ollama(model="phi3-medium")