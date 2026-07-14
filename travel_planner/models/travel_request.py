
from pydantic import BaseModel, ValidationError , field_validator
from datetime import date

 
class Traveller(BaseModel):
    name : str
    age : int
    destination : str
    origin : str
    budget : int
    no_of_travellers : int
    

    
    @field_validator("age")
    @classmethod
    def check_age(cls, value):

        if value < 18 :
            raise ValueError (" Bhai thode aur bade ho jaao tab ghoomna .")
        return value
            
    
    
    @field_validator("budget")
    @classmethod
    def check_budget(cls, value):
        if value <=2000 :
            raise ValueError (" Bhai aap gareeb ho , thode aur ameer ho jaao tab ghoomna . 😒😒")
        return value
    
    
    @field_validator("no_of_travellers")
    @classmethod
    def check_no_of_travellers(cls, value):
        if value <=0 :
            raise ValueError (" Bhai aapka bhoot jaayega kya ghoomne 😒 .")
        return value


try:
    age = input("Enter your age sir : ")
    
    name = input("Enter your name sir : ")
    destination = input("Enter your destination sir : ")
    origin = input("Enter your origin sir : ")
    budget  = input("Enter your budget sir : ")
    no_of_travellers = input("Enter no of travellers sir : ")



    traveller = Traveller(age=age,
                          name = name,
                          origin = origin,
                          destination = destination,
                          budget = budget,
                          no_of_travellers= no_of_travellers,
                          )
    print("\nData recieved Successfully .!!")
    print("Our team will contact you soon !!")
    print(traveller)

except ValidationError as e:
    print("\nValidationError")
    print(e)
    








   

