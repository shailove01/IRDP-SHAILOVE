from prompts.travel_prompts import transportation_prompt
from models.schemas import TransportationSchema
from models.travel_state import TravelState
from services.llm_service import LLMService

llm = LLMService()

def transportation_node(state: TravelState) -> TravelState:
    prompt = transportation_prompt(
        origin=state["origin"],
        destination= state["destination"],
        budget= state["budget"],
          travellers= state["travellers"]  )
    
    response = llm.generate_structured(
    prompt = prompt, 
    schema = TransportationSchema)

    return {
        "transport_mode" : response.transport_mode,
        "transport_cost" : response.transport_cost,
        "transport_reason": response.reason
    }