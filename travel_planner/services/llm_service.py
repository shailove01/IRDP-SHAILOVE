from langchain_groq import ChatGroq
from config import One

class LLMService:

    def __init__(self):
        self.llm = ChatGroq(
            api_key=One.GROQ_API_KEY,
            model_name=One.MODEL_NAME,
            temperature=One.TEMPERATURE)

    def generate(self, prompt):
        response = self.llm.invoke(prompt)
        return response.content
    def generate_structured(self, prompt, schema):
        structured_llm = self.llm.with_structured_output(schema)
        response = structured_llm.invoke(prompt)
        return response

#check for api key missing
# check for internet 
# check rate limit
