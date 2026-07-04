# Q1. Positive or Negative

# Take a number as input.

# Print:

# "Positive" if the number is greater than 0.
# "Negative" if the number is less than 0.

# Solution:- 

x=int(input("Enter a number : "))
if (x<0):
    print(x,"is a negative number.")
else:
    print(x, "is a positive number.")


# ______________________________________________________________________

# Q2. Even or Odd

# Take an integer from the user.

# Print:

# "Even"
# "Odd"

# Solution:- 


x=int(input("Enter a number : "))
if(x%2==0):
    print(x,"is an even number .")
else:
    print(x,"is an odd number .")

# _________________________________________________________________________


# Q3. Vote Eligibility

# Take age as input.

# Print:

# "Eligible to Vote" if age is 18 or above.
# "Not Eligible" otherwise.

# Solution:-

x=int(input("Enter your age : "))

if (x>=18):
    print("You're eligible to vote.")
else:
    print("Not Eligible .")


# _______________________________________________________________________________

# 4. Pass or Fail

# Take marks as input.

# Rules:

# Marks ≥ 33 → Pass
# Otherwise → Fail


# Solution :- 

marks=int(input("Enter your marks : "))

if(marks>=33):
    print("Pass")
else:
    print("Fail")

# ___________________________________________________________________

# Take a year.

# Print:

# Leap Year

# or

# Not a Leap Year

# (Hint: A leap year is divisible by 4,
#  but years divisible by 100 are not leap years
#  unless they are also divisible by 400.)

# Solution:-

year=int(input("Enter the year : "))

if(year%400==0 or year%4==0 ):
    print("leap year")

else:
    print("Not a leap year .")


# ___________________________________________________________

# Q9. Character Check

# Take one character.

# Print whether it is:

# Alphabet
# Digit
# Special Character

# Solution:-

ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

x=input("Enter items : ")



