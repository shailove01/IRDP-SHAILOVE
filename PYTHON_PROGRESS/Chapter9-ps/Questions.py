

# Q1 :- 
# Create a class 'Pets' from a class 'Animals' and further create 
# a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'.

# Solution :- 

# class Animals:
#     pass


# class Pets(Animals):
#     pass


# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Bhauu Bhauuu")

# D= Dog()
# D.bark()
    


'''
Q2. Store Data in an Object

Create a class Student.

Inside __init__(), store:

name
age

Create an object:

student1 = Student("Shailove", 22)

Print

Name: Shailove
Age: 22
'''


# class Student:
#     def __init__(self, name , age ):
#         self.name = name 
#         self.age = age     
        
# student1 = Student("Shailove", 22)

# print(student1.name)
# print(student1.age)





# # Q3:- 



# class Student:
#     def __init__(self, name , age ):
#         self.name = name 
#         self.age = age 
        
#     def introduce(self ):
#         print(f"Hello, my name is {self.name}.")
#         print(f"I am {self.age} years old.")
        
        
        
# student1 = Student("Shailove", 22)
# student2 = Student("Raam Laal", 25)
# student1.introduce()
# student2.introduce()
        


# Question 4 (Easy → Medium)
# Ab coding question.
# Bank Account
# Ek class banao:
# class BankAccount:
# __init__() me store karo:
# account_holder
# balance
# 3 methods banao:
# deposit(amount)
# withdraw(amount)
# show_balance()
# Rules
# deposit() balance me amount add kare.
# withdraw() balance se amount minus kare.
# Agar withdraw amount balance se zyada ho to print karo:
# Insufficient Balance
# aur balance change nahi hona chahiye.

# Example
# acc = BankAccount("Shailove", 1000)
# acc.deposit(500)
# acc.show_balance()
# acc.withdraw(200)
# acc.show_balance()
# acc.withdraw(2000)
# Expected output:
# Current Balance: 1500
# Current Balance: 1300
# Insufficient Balance


# class BankAccount:
#     def __init__(self, acc_holder, balance ):
#         self.acc_holder = acc_holder
#         self.balance =  balance
        

#     def deposit(self):
#         return (amount+self.balance)
#     def withdraw(self):
#         if (w_amount > self.balance) :
#             print("Withdraww exceeds balance amount.")
#         else:
#             return (self.balance - amount)
#     def show_balance(self):
#         print(self.balance)

# acc = BankAccount("Shailove", 1000)
# print("1 for deposit :")
# print("2 for withdraw :")
# print("3 for balance check :")
# x=int(input("Enter your choice : "))

# if (x==1):
#     amount=int(input("Enter the amount you want to deposit :"))
#     print(acc.deposit())
# elif (x==2):
#     amount=int(input("Enter the amount you want to withdraw :"))
#     w_amount = amount
#     print(acc.withdraw())
# elif(x==3):
#     print(acc.show_balance())

# else : 
#     print("BHII AAPKE PAAS PAISE HI NHI HAI ...GAREEB😒")
    




# class Student:
#     def __init__(self, name , marks ):
#         self.name = name 
#         self.marks = marks 
        

#     def update_marks(self,new_marks):
#         print(f"You have changed marks from {self.marks} to {new_marks}")
#         self.marks=new_marks
#     def display(self):
#         print("Name : ",self.name)
#         print("Marks : ", self.marks)
#     def is_pass(self):
#         if(self.marks >= 33):
#             print("Result : Pass")
#         else:
#             print("Result : Fail")




# student1 = Student("Shailove Singh", 99)
# student1.display()
# student1.is_pass()
# student1.update_marks(100)

# student1.display()

# ___________________________________________________________________________________

# Smart Employee Management System
# Ek IT company apne employees ko manage karna chahti hai.
# Company me 3 tarah ke employees hain:
# Software Developer
# Manager
# Intern

# Har employee ke paas common information hogi:
# Employee ID
# Name
# Basic Salary

# Lekin salary calculate karne ka rule sabke liye alag hai.
# Salary Rules
# Software Developer
# Basic Salary + Project Bonus
# Manager
# Basic Salary + Team Bonus + Performance Bonus
# Intern
# Fixed Stipend

# Features
# Employee details show karo.
# Final salary calculate karo.
# Company ke saare employees ko ek list me store karo.
# Ek hi function se sabki salary print karo.

# Constraints
# Future me company naye employee types add kar sakti hai.
# Existing code me minimum changes hone chahiye.
# 🤏 Hint

# Socho...
# Agar future me HR Designer Tester bhi add ho jayein,
# to tumhara code kitna change hoga?


















class Company :
    def __init__(self, soft_dev, manager, intern):
        self.soft_dev = soft_dev
        self.manager = manager
        self.intern = intern
class Employee():
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def salary_calculate(self):
        
        if(designation == 1):
            total = (self.basic_salary + project_bonus)
            print(f"Final salary of SD is : ", total)
        elif(designation == 2):
            total1 = (self.basic_salary + team_bonus + performance_bonus)
            print(f"Final salary of Manager is : ", total1)
        elif(designation == 3):
            print(f"Final salary of Intern is : ", fixed_stipend)
                  

emp = Employee(1,"Shailove Singh", 25000)
print("For software developer enter 1: ")      
print("For manager enter 2: ")      
print("For intern enter 3: ") 
project_bonus = 2000
team_bonus = 1000
performance_bonus = 2000
fixed_stipend = 5000     
basic_salary = 25000
designation = int(input("Enter Designation : "))
print(emp.emp_id)
print(f"Employee Name : {emp.name}")
print(f"Basic Salary : {emp.basic_salary}")
print(emp.salary_calculate())


