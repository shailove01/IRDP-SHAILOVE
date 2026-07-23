from models.travel_state import TravelState
from models.schemas import SummarySchema
from prompts.travel_prompts import summary_prompt
from services.llm_service import LLMService


llm = LLMService()
def summary_node(state: TravelState) -> dict:
    prompt = summary_prompt(
        prefrence= state["prefrence"],
        destination=state["destination"],
        destination_type=state["destination_type"],
        transport_mode=state["transport_mode"],
        hotel_name=state["hotel_name"],
        total_cost=state["total_cost"],
        budget_status = state["budget_status"],
        optimization_reason = state["optimization_reason"],
        top_attractions=state["top_attractions"],
        travel_tips=state["travel_tips"],
        packing_list=state["packing_list"])

    response = llm.generate_structured(
        prompt=prompt,
        schema=SummarySchema)
    return {"trip_summary": response.summary}