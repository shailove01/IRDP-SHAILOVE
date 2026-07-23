from models.travel_state import TravelState

def budget_router(state : TravelState) -> str:
    if (state['budget_status'] == "Within Budget"):
        return "within_budget"
    elif(state['budget_status'] == "Over Budget"):
        return "over_budget"
