import os 
from dotenv import load_dotenv
load_dotenv()

class One:
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        MODEL_NAME = os.getenv("MODEL_NAME")
        TEMPERATURE = os.getenv("TEMPERATURE")
        TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    