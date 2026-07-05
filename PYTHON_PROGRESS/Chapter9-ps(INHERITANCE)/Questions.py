

# Q1 :- 
# Create a class 'Pets' from a class 'Animals' and further create 
# a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'.

# Solution :- 

class Animals:
    pass


class Pets(Animals):
    pass


class Dog(Pets):
    @staticmethod
    def bark():
        print("Bhauu Bhauuu")

D= Dog()
D.bark()
    
