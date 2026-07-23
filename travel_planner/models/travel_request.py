from pydantic import BaseModel, field_validator


class Traveller(BaseModel):
    name: str
    age: int
    origin: str
    budget: int
    travellers: int
    prefrence : str

    @field_validator("age")
    @classmethod
    def check_age(cls, value):
        if value < 18:
            raise ValueError("Bhai thode aur bade ho jaao tab ghoomna.")
        return value

    @field_validator("budget")
    @classmethod
    def check_budget(cls, value):
        if value <= 2000:
            raise ValueError("Budget should be greater than 2000.")
        return value

    @field_validator("travellers")
    @classmethod
    def check_no_of_travellers(cls, value):
        if value <= 0:
            raise ValueError("Number of travellers should be greater than 0.")
        return value