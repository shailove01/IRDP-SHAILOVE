from langgraph.graph import StateGraph, START, END
from models.travel_state import TravelState
from nodes.destination_node import destination_node
from nodes.hotel_node import hotel_node
from nodes.packing_node import packing_node
from nodes.summary_node import summary_node
from nodes.transportation_node import transportation_node
from nodes.cost_node import cost_node
from nodes.attractions_node import attractions_node
from nodes.travel_tips import travel_tips_node
from routers.budget_router import budget_router
from nodes.budget_optimizer_node import budget_optimizer_node



workflow = StateGraph(TravelState)
workflow.add_node("destination", destination_node)
workflow.add_node("transportation", transportation_node)
workflow.add_node("attractions", attractions_node)
workflow.add_node("hotel", hotel_node)
workflow.add_node("cost", cost_node)
workflow.add_node("budget_optimizer", budget_optimizer_node)
workflow.add_node("travel_tips", travel_tips_node)
workflow.add_node("packing", packing_node)
workflow.add_node("summary", summary_node)




workflow.add_edge(START, "destination")
workflow.add_edge("destination","transportation")
workflow.add_edge("transportation", "hotel")
workflow.add_edge("hotel","cost" )
workflow.add_conditional_edges("cost", budget_router,
                               {"within_budget": "attractions",
                                "over_budget" : "budget_optimizer"})
workflow.add_edge("budget_optimizer", "cost")
workflow.add_edge("attractions", "travel_tips")
workflow.add_edge("travel_tips", "packing")
workflow.add_edge("packing", "summary")
workflow.add_edge("summary", END)

travel_graph = workflow.compile()