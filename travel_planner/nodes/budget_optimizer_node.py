from models.travel_state import TravelState
from services.llm_service import LLMService
from models.schemas import BudgetOptimizerSchema
from prompts.travel_prompts import budget_optimizer_prompt


llm = LLMService()

def budget_optimizer_node(state : TravelState) -> TravelState:
    prompt = budget_optimizer_prompt(
        budget = state["budget"],
        transport_mode = state["transport_mode"],
        hotel_name = state["hotel_name"],
        destination = state["destination"],
        total_cost = state["total_cost"]
    )

    response = llm.generate_structured(
        prompt=prompt,
        schema=BudgetOptimizerSchema
    )

    return{
        "transport_mode": response.transport_mode,
        "transport_cost" : response.transport_cost,
        "hotel_name" : response.hotel_name,
        "hotel_cost" : response.hotel_cost,
        "optimization_reason" : response.optimization_reason 
    }