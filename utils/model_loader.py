from pydantic import BaseModel, Field
import os
from typing import Literal, Optional, Any
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from utils.config_loader import load_config
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings


class ConfigLoader:
    def __init__(self):
        print(f"Loaded config...")
        self.config = load_config()
    
    def __getitem__(self,key):
        return self.config[key]
    
    

class ModelLoader(BaseModel):
    model_provider: Literal["openai", "groq"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)
    
    def model_post_init(self,__context:Any)->None:
        self.config = ConfigLoader()
        
    class Config:
        arbitrary_types_allowed = True
        
    def load_llm(self):
        """
        Load and run the LLM Model.
        """
        print("LLM Loading....")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading Groq model...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model=model_name, api_key=groq_api_key)
        elif self.model_provider == "openai":
            print("Loading openai model....")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(model_name=model_name, api_key=openai_api_key)
            
        return llm
            
        
    
    
        