from services.llm_service import LLMService
from models.travel_state import TravelState
from prompts.travel_prompts import attractions_prompt
from models.schemas import AttractionsSchema

llm = LLMService()

def attractions_node(state : TravelState) -> TravelState:
    prompt = attractions_prompt(
        destination = state["destination"],
        budget = state["budget"],
        travellers = state["travellers"]

    )

    response = llm.generate_structured(
        prompt=prompt,
        schema=AttractionsSchema
    )

    return{
        "top_attractions" : response.top_attractions,
        "attraction_reason" : response.attraction_reason
    }