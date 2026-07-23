from pydantic import BaseModel, Field


class DestinationSchema(BaseModel):
    destination: str = Field(description="Best travel destination according to user's budget .")
    destination_type : str = Field(description="Type of destination such as Beach, Mountain, City or Hill Station.")
    reason: str = Field(description="Reason why this destination is recommended.")


class HotelSchema(BaseModel):
    hotel_name : list[str] = Field(description="Names of Top Hotels.")
    hotel_cost : int = Field(description = "Cost of the Hotels .")
    reason: str = Field(description="Reason why these hotels are recommended.")


class PackingSchema(BaseModel):
    packing_list: list[str] = Field(
        description="Items required during the trip.")

class SummarySchema(BaseModel):
    summary: str = Field(
        description="Complete summary of the travel plan.")
    
class TransportationSchema(BaseModel):
    transport_mode : str
    transport_cost : int
    reason : str = Field(description = "Reason why this transportation mode is recommended.")

class CostSchema(BaseModel):
    food_cost : int
    activity_cost : int
    misc_cost : int

class BudgetOptimizerSchema(BaseModel):
    transport_mode : str
    transport_cost : int
    hotel_name : str
    hotel_cost : int
    optimization_reason : str
    
    
class AttractionsSchema(BaseModel):
    top_attractions : list[str]
    attraction_reason : str = Field(description = "Reason , why the places are recommended .")

class TravelTipsSchema(BaseModel):
    travel_tips : list[str]
