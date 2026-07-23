from models.travel_state import TravelState
from models.schemas import PackingSchema
from prompts.travel_prompts import packing_prompt
from services.llm_service import LLMService


llm = LLMService()
def packing_node(state: TravelState):
    prompt = packing_prompt(
        destination=state["destination"])
    response = llm.generate_structured(
        prompt=prompt,
        schema=PackingSchema)
    return {
        "packing_list": response.packing_list}