# Q1.

# Create variables to store:

# Your name
# Your age
# Your height
# Whether you are a student

# Print all four.
# ____________________________________________________________________________


# #Solution :- 


x=str(input("Enter Your Name : " ))
y=int(input("Enter Your Age : " ))
z=float(input("Enter Your Height : " ))
a=str(input("Whether you're a student or not ? : " ))

print( x,"\n","\n", y ,"\n",z ,"\n",a)

# ____________________________________________________________________________


# Q2.

# Create two variables:
# Print their sum, difference, product, and division.
# _________________________________________________________________________________________________________

# # Solution


a=10
b=20
dif=a-b
print(dif)


# ________________________________________________________________________________________________________

# Q6.

# Take two numbers as input and print:

# Sum
# Difference
# Product
# Division

# Solution


a=10
b=5
dif= a-b
mul = a*b
add=a+b
div=a/b

print( " ",dif,"\n",mul,"\n",add,"\n",div)


# _______________________________________________________________________________________


# Q7.

# Why does this code fail?

# age = input("Enter age: ")
# print(age + 5)

# Fix it.


age = int(input("Enter age: "))
print(age + 5)


# __________________________________________________________________________________

# Q9.

# Take a decimal number from the user and print its datatype before and after typecasting.

# Example:

# Input:
# 12.5

# Output should show:

# <class 'str'>
# <class 'float'>

# Solution:

x = float(input(" Enter your number : "))
a= type(x)
print(a)
y=str(a)
g=type(y)
print(g)

# __________________________________________________________________________

# Q10.

# Convert

# num = 25

# to

# float
# string
# boolean

# and print all.

num=25
x=float(num)
y=type(x)
print(y)
p=str(num)
q=type(p)
print(q)
r=bool(num)
t=type(r)
print(t)


# _____________________________________________________________________


# Q12.

# Without calculating mentally, write the output of:

# print(10 // 3)
# print(10 % 3)
# print(2 ** 5)


# Solution:
print(10 // 3)
print(10 % 3)
print(10 ** 3)

# _______________________________________________________________

# Q13.

# Take two numbers from the user and 
# print which one is greater.

# Solution:

x=int(input("Enter your first number : "))
y=int(input("Enter Second Number : "))
if(x>y):
    print("Greater number is : ",x)
else:
    print(y,"is greater number. ")


# _____________________________________________________________________

# Q16.

# Take your birth year as input 
# and calculate your age.


# Solution :

dob = int(input("Enter your date of birth : "))
py=int(input("Enter present year : "))

curr_age=py-dob
print(curr_age)


# __________________________________________________________________________

# Q18.

# Take temperature in Celsius.

# Convert to Fahrenheit.

# Formula:

# F = (C × 9/5) + 32

# Solution : 

temp=float(input("Enter temperature in celsius :"))
f_temp= (temp * 9/5)+32
print(f_temp)


# ______________________________________________________________________________________

# Q19.

# Take a bill amount.

# Add 18% GST.

# Print final amount.


# Solution:

x=float(input("Enter your bill amount : "))
y = x+18%x
print(y)


# ________________________________________________________________________________________

# 20. ⭐ Challenge

# Take three numbers from the user.

# Print:

# Largest number
# Smallest number
# Average

# Solution : 

first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
third = int(input("Enter third number : "))

if(first>second and first> third):
    print(first, "is greater")
elif(second>first and second > third):
    print(second , "is greater ")
else :
    print(third, "is greater ")

if (first < second and first < third ):
    print (first, "is smaller ")
elif(second < first and second < third):
    print(second, "is smaller ")
else :
    print(third, "is smalller ")
sum = first+second+third
average = sum / 3

print("Average = ", average )
    