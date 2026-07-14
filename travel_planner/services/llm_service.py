
from langchain_groq import ChatGroq
from config import One

class LLMProvider :
    def __init__(self):
        self.llm = ChatGroq(
        api_key=One.GROQ_API_KEY,
        model_name=One.MODEL_NAME,
        temperature=One.TEMPERATURE
        )
    def generate_response(self, prompt):
        response = self.llm.invoke(prompt)
        return response.content 


#check for api key missing
# check for internet 
# check rate limit
