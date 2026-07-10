class Dog:
    def __init__(self , name, breed, Owner):
        self.name = name
        self.breed = breed
        self.Owner = Owner


    def bark(self):
        print("Bhaau Bhaau")

class Owner(Dog):
    def __init__(self, Oname , mobile):
        self.Oname = Oname
        self.mobile = mobile


dog1= Dog("Kaluaa" ,"Golden_Retriever" )
owner1 = Owner("Rampal Yadav", 102)
print(f"{dog1.name}  hai { dog1.breed} 😎")
print(owner1.Oname)
print(owner1.mobile)


dog2=Dog("Chhotu", "St. Bernard")
owner2 = Owner("paaji", 112)
print(dog2.name , dog2.breed)
print(f" Jiska Owner hai {owner2.Oname}")
print(owner2.mobile)

