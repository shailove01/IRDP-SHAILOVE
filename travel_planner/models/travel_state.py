from typing import TypedDict


class TravelState(TypedDict):

    
    name: str
    age: int
    origin: str
    budget: int
    travellers: int
    prefrence : str

    transport_mode : str
    transport_cost : int
    transport_reason : str

    food_cost: int
    activity_cost: int
    misc_cost: int
    total_cost: int

    budget_status : str

    
    destination: str
    destination_type : str
    destination_reason: str
    optimization_reason : str


    top_attractions :list[str] 
    attraction_reason : str 

    travel_tips :  list[str]
    
    hotel_name: list[str]
    hotel_cost: int
    hotel_category : str 

    packing_list: list[str]

    trip_summary: str