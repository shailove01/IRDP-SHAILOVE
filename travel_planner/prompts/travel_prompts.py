def destination_prompt(name: str,age: int,origin: str,
        budget: int,
            travellers: int,  prefrence : str) -> str:

 return f"""
You are an experienced AI Travel Planner.

Your task is to recommend the SINGLE BEST travel destination for the user.

User Details
------------
Name: {name}
Age: {age}
Origin: {origin}
Budget: ₹{budget}
Number of Travellers: {travellers}
Travel Preference: {prefrence}

Instructions
------------
1. The user's travel preference is the HIGHEST priority.
2. Recommend ONLY ONE destination.
3. Do NOT repeatedly recommend the same destination (e.g., Manali) unless it is genuinely the best choice.
4. Consider:
   - User's travel preference
   - Budget
   - Number of travellers
   - Distance from origin
   - Overall travel experience
5. Recommend a destination that is realistically affordable within the given budget.
6. Avoid random or generic recommendations.
7. Explain clearly WHY this destination matches the user's preferences.

Examples
--------
If preference is Beach:
- Goa
- Gokarna
- Pondicherry
- Andaman

If preference is Mountains:
- Manali
- Shimla
- Kasol
- Mussoorie
- Auli

If preference is Desert:
- Jaisalmer
- Bikaner

If preference is Forest:
- Jim Corbett
- Ranthambore

If preference is City:
- Jaipur
- Udaipur
- Mumbai
- Bengaluru

Return ONLY the following fields:

destination: string
destination_type: string
reason: string
"""



def transportation_prompt(origin : str , destination : str,
                          budget : int,  travellers : int) -> str:
    return f"""
You are a transport recommendation expert.

Origin: {origin}
Destination: {destination}
Budget: {budget}
Travellers: {travellers}

Recommend the best transportation considering budget, distance, comfort and travel time.

Return ONLY these fields:

1. transport_mode (string)
2. transport_cost (integer only, do NOT use quotes, currency symbols or commas)
3. reason (string)
"""



def attractions_prompt(destination : str , budget : int , travellers : int ):
    return f""" Recommend top five places near the user's destination.

"destination" : {destination}
"budget" : {budget}
"travellers" : {travellers} 

Return:
1. Top Attractions according to the prefrence.
2. Reason
"""




def travel_tips_prompt(destination : str , travellers :int ):
    return f"""You are an experienced travel guide.

Destination: {destination}

Number of Travellers: {travellers}

Provide 5 to 7 practical travel tips related to:
- Safety
- Local transportation
- Weather
- Clothing
- Local customs (if applicable)

Return:
1. Travel Tips
"""



def cost_prompt(
    transport_cost: int,
    hotel_cost: int,
    destination: str,
    travellers: int
):
    return f"""Estimate realistic travel expenses for the given destination.
      You will give the user approximate cost of the things as defined .

Travel Details:

Destination: {destination}
Travellers: {travellers}
Transportation Cost: {transport_cost}
Hotel Cost: {hotel_cost} 

Return ONLY these fields:

1. food_cost (integer)
2. activity_cost (integer)
3. misc_cost (integer)

Do NOT calculate total_cost.
Do NOT include transport_cost or hotel_cost in these values.
Return only valid JSON.
"""




def hotel_prompt(destination: str, budget: int) -> str:
    return f"""You are a hotel recommendation expert.
Destination: {destination}
Budget: ₹{budget}
Recommend the best hotels under budget.
Return only required fields.
Also provide a short reason for your recommendation.
"""



def budget_optimizer_prompt(budget : int , total_cost : int,
                            transport_mode : str, 
                            hotel_name: str, 
                            destination : str) :
    return f""" You are an efficient travel budget optimizer. 
    If the total cost already exceeds the budget then you have to make sure to do the below tasks :-  
    Your priority goal is to optimize the costs of the itinerary.
    You have to optimize the cost of the itinerary by finding alternate solutions with less cost and if not possible you have to make the total cost closest affordable.
    The details of the current itinerary are defined below : 
Budget : {budget}
Destination : {destination}
Transport Mode : {transport_mode}
Hotel Name : {hotel_name}
Total Cost : {total_cost}
Optimize the transport and hotel .
Destination will remain unchanged.
Return the best alternatives for reducing the total cost only for the required fields.
Return a valid JSON
Make sure to reduce the cost without degrading the user's travel experience.
Also provide the reason for the new alternatives you will decide and no extra explanation.
"""




def packing_prompt(destination: str) -> str:
    return f"""Create a packing checklist.
Destination: {destination}
Return only the important packing items.
"""





def summary_prompt(
    prefrence : str,
    destination: str,
    destination_type : str,
    transport_mode : str,
    hotel_name: str,
    total_cost : int, 
    budget_status : str,
    optimization_reason : str,
    top_attractions : list[str],
    travel_tips : list[str],
    packing_list: list[str]) -> str:
   
    return f"""
You are an experienced travel planner.

Using the travel details below, generate a concise travel summary.
Travel Details:
- Prefrence : {prefrence}
- Destination:{destination}
- Destination Type : {destination_type}
- Transportation : {transport_mode}
- Selected Hotel :{hotel_name}
- Cost : {total_cost}
- Budget Status: {budget_status}
- Current Transportation : {transport_mode}
- Current Hotel : {hotel_name}
- Current Budget : {budget_status}
- Current Total Cost : {total_cost}
- Optimization Reason : {optimization_reason}
- Top Attractions : {top_attractions}
- Travel Tips : {travel_tips}
- Packing List:{packing_list}

Instructions:
- Write ONE summary string.
- Keep it under 120 words.
- Mention budget status.
- If budget status is "Over Budget", suggest choosing a budget hotel or cheaper transport.
- If budget status is "Within Budget", mention that the trip fits the budget.
- Do not use markdown headings.

"""