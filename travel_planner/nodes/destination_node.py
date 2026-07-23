from models.travel_state import TravelState
from models.schemas import DestinationSchema
from prompts.travel_prompts import destination_prompt
from services.llm_service import LLMService


llm = LLMService()


def destination_node(state: TravelState):
    prompt = destination_prompt(
        name=state["name"],
        age=state["age"],
        origin=state["origin"],
        budget=state["budget"],
        travellers=state["travellers"],
        prefrence = state["prefrence"])

    response = llm.generate_structured(
        prompt=prompt,
        schema=DestinationSchema)

    return {
        "destination": response.destination,
        "destination_type": response.destination_type,
        "destination_reason": response.reason}