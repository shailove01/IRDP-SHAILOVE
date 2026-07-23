from workflow.workflow import travel_graph
from models.travel_request import Traveller


def main():
    try:
        
        # User Input
        
        traveller = Traveller(
            name=input("Enter Name: "),
            age=int(input("Enter Age: ")),
            origin=input("Enter Origin: "),
            budget=int(input("Enter Budget: ")),
            travellers=int(input("Enter Number of Travellers: ")),
            prefrence = input(" Prefrences : \n - Beach \n - Mountains \n - Desert \n - Forest \n - Hill Station \n - City \n Enter Your Prefrence : ")
        )

        
        # Initial State
        
        initial_state = {
            "name": traveller.name,
            "age": traveller.age,
            "origin": traveller.origin,
            "budget": traveller.budget,
            "travellers": traveller.travellers,
            "prefrence" : traveller.prefrence
        }

        
        # Run LangGraph Workflow
       
        result = travel_graph.invoke(initial_state)

################################################################################
        
        # Display Result
        
        print("\n" + "=" * 60)
        print("           AI TRAVEL PLANNER REPORT")
        print("=" * 60)

        print(f"\n Traveller : {result['name']}")
        print(f" Origin    : {result['origin']}")

################################################################################
        print("\n" + "=" * 60)
        print("           DESTINATION DETAILS..")
        print("=" * 60)

        print(f"\n Destination      : {result['destination']}")
        print(f" Destination Type : {result['destination_type']}")
        print(f" Reason           : {result['destination_reason']}")

################################################################################
        print("\n" + "=" * 60)
        print("           TRANSPORTATION DETAILS..")
        print("=" * 60)


        print(f"\n Transportation : {result['transport_mode']}")
        print(f" Transport Cost : ₹{result['transport_cost']}")
        print(f" Reason         : {result['transport_reason']}")

################################################################################
        print("\n" + "=" * 60)
        print("           HOTEL DETAILS..")
        print("=" * 60)


        print(f"\n Hotel : {result['hotel_name']}")
        print(f" Hotel Cost : ₹{result['hotel_cost']}")
################################################################################

        print("\n" + "=" * 60)
        print("           EXPENDITURE")
        print("=" * 60)

        print(f"   Food Cost      : ₹{result['food_cost']}")
        print(f"   Activity Cost  : ₹{result['activity_cost']}")
        print(f"   Misc Cost      : ₹{result['misc_cost']}")
        print(f"   Total Cost     : ₹{result['total_cost']}")

################################################################################
        print("\n" + "=" * 60)
        print("           BUDGET ANALYSIS")
        print("=" * 60)
        print(f"    Budget        : ₹{result['budget']:,} ")
        print(f"    Estimated Cost: ₹{result['total_cost']:,} ")
        print(f"    Status        :  {result['budget_status']}")
################################################################################

        print("\n" + "=" * 60)
        print("           TOP PLACES")
        print("=" * 60)

        for i, place in enumerate(result["top_attractions"], start=1):
            print(f"{i}. {place}")

################################################################################

        print("\n" + "=" * 60)
        print("           ATTRACTION REASON..")
        print("=" * 60)

        print(f"\n Attraction Reason")
        print(result["attraction_reason"])

################################################################################
        print("\n" + "=" * 60)
        print("           TRAVEL TIPS")
        print("=" * 60)

        for i, tip in enumerate(result["travel_tips"], start=1):
            print(f"{i}. {tip}")


################################################################################
        print("\n" + "=" * 60)
        print("           PACKING TO DO..")
        print("=" * 60)

        for i, item in enumerate(result["packing_list"], start=1):
            print(f"{i}. {item}")

################################################################################
        print("\n" + "=" * 60)
        print("           TRIP SUMMARY")
        print("=" * 60)

        print(result["trip_summary"])

        print("\n" + "=" * 60)

################################################################################
    except Exception as e:
        print("\n Error:", e)


if __name__ == "__main__":
    main()