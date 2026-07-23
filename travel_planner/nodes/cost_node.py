from services.llm_service import LLMService
from models.schemas import CostSchema
from models.travel_state import TravelState
from prompts.travel_prompts import cost_prompt


llm = LLMService()

def cost_node(state : TravelState) -> dict:
    prompt = cost_prompt(
        
        transport_cost = state["transport_cost"],
        hotel_cost = state["hotel_cost"],
        destination = state["destination"],
        travellers = state["travellers"]
    )
    response = llm.generate_structured(
        prompt=prompt,
        schema=CostSchema
    )

    total_cost =( state["transport_cost"] 
    + state["hotel_cost"]
    + response.food_cost
    + response.activity_cost 
    + response.misc_cost
    )
    if (total_cost >state["budget"]):
        budget_status = "Over Budget"
        
    else :
        budget_status = "Within Budget" 

    return{
        "food_cost" : response.food_cost,
        "activity_cost" : response.activity_cost,
        "misc_cost" : response.misc_cost,
        "total_cost": total_cost,
        "budget_status" : budget_status
    }
