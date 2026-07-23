from models.travel_state import TravelState
from models.schemas import HotelSchema
from prompts.travel_prompts import hotel_prompt
from services.llm_service import LLMService


llm = LLMService()
def hotel_node(state: TravelState):
    prompt = hotel_prompt(
        destination=state["destination"],
        budget=state["budget"])
    response = llm.generate_structured(
        prompt=prompt,
        schema=HotelSchema)
    return {
        "hotel_name": response.hotel_name,
        "hotel_cost": response.hotel_cost
        }

