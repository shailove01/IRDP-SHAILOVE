from services.llm_service import LLMService
from models.travel_state import TravelState
from prompts.travel_prompts import travel_tips_prompt
from models.schemas import TravelTipsSchema

llm =  LLMService()

def travel_tips_node(state : TravelState) -> str :
    prompt = travel_tips_prompt(
        destination= state["destination"],
        travellers=state["travellers"]
    )

    response = llm.generate_structured(
        prompt=prompt, 
        schema=TravelTipsSchema
    )

    return {
        "travel_tips": response.travel_tips
    }