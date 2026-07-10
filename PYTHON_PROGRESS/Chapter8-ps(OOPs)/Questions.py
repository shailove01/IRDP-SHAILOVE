
# # Q1:- 

# # Create a class programmer for storing information 
# # of few programmers working at Microsoft.

# # Solution :- 

class Programmer:
    company = "Microsoft"
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary

s=Programmer("Shailove", 1200545)
print(s.name, s.salary)


# # Q2 :-

# # Write a class "calculator" capable of finding squares,
# # cube and square root of a number.


# # Solution :- 

class Calculator:

    def __init__(self, n, c):
        self.n = n
        self.c = c

    def square(self):
        return f"The square of {self.n} is {self.n * self.n}"

    def add(self):
        return f"The addition of {self.n} and {self.c} is {self.n + self.c}"

    def mul(self):
        return f"The multiplication of {self.n} and {self.c} is {self.n * self.c}"

    def diff(self):
        return f"The difference of {self.n} and {self.c} is {self.n - self.c}"


a = Calculator(10, 5)

print(a.square())
print(a.add())
print(a.mul())
print(a.diff())




# Q3 :- 

# Write a class train which has methods to book a ticket, 
# get status and get fare info. if train rinning under Indian Railways.

# Solution :- 
from random import randint

class Train:

    def __init__(self , trainNo):
        self.trainNo = trainNo
        
       
    def book(self , frm , to):
        self.frm = frm
        self.to = to
        return(f"ticket is booked from {frm} -- {to}")
    def status(self):
        return(f"Your train {self.trainNo} is at platrom number : {(randint(10 ,16))}")
    def fare(self):
        return(f"ticket fare from {self.frm}--{self.to} is : {randint(100 , 1000)}")

frm = str(input("Enter boarding station : "))
to = str(input("Enter destination station : "))

a = Train(trainNo = 14252)
print(a.book(frm, to))
print(a.status())
print(a.fare())



# Q4 :- 
# Can you change the self parameter inside a class to something else .
# Try changing to "sit" or "shailove" and see the effects.

# Solution :- 

