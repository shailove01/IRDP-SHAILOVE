# Write a program to find greatest of three numbers.

def greatest(x,y,z):
    if(x>y and x>z):
        print(x,"is greater.")
    elif(y>x and y>z):
        print(y, "is greater number.")
    else:
        print(z, "is a greater number.")


x=int(input("First number : "))
y=int(input("Second number : "))
z=int(input("Third number : "))
greatest(x,y,z)



# 2:- farenheight to degree celsius

def faren_to_cel(f):
    return(5*(f-32)/9)
f=int(input("Enter Farenheight value : "))
print(round(faren_to_cel(f) ,2  ))


# 3: Sum of Natural numbers.

def nat_num(n):
    if(n==1):
        return 1
    return nat_num(n-1) + n
n=int(input("Enter a Number : "))
print(nat_num(n))


# 4:- Print star pattern 
#   * * *
#   * *
#   *

# Solution:- 

def star(n):
    if(n==0):
        return
    print("*" * n)
    star(n-1)
    
n=int(input("Enter the number : "))
star(n)


# 5:- Write a python program to convert inches to centimetres.

# Solution:-

def convert(n):
    return n*2.5
n=int(input("Enter the centimeter value : "))
print(convert(n))



# Q6. Square of a Number
# Create a function that accepts 
# one number and prints its square.
# Example:
# Input:
# 5
# Output:
# 25

# Solution:-

def square(n):
    return n*n
n=int(input("Enter Your Number : "))
print(square(n))


# Q7. Even or Odd

# Create a function that accepts one number.
# Print:
# Even Number
# or
# Odd Number

def even_odd(n):
    if(n%2==0):
        return "Even Number."
    else:
        return "Odd Number."
n=int(input("Enter your Number : "))
print(even_odd(n))



# Q6. Multiplication Table
# Create a function that accepts one number 
# and prints its table up to 10.

# Example:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

# Solution:-

def mul_table(n):
    if(n==0):
        return
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
        i=i+1
n=int(input("Enter a Number : "))
mul_table(n)




# Q10. Largest Number in a List

# Create a function that accepts a list
# and returns the largest element.
# Example:
# Input:
# [5, 2, 10, 8]
# Output:
# 10

# Solution:- 

def largest(l):
    l.sort(reverse=True)
    print(l[0])

l=[2,4,7,4,6,7,9,8,10,4,3,21]
largest(l)




# Q11. Sum of List

# Create a function that accepts a list and returns
# the sum of all elements.

# Solution :-

def sum_list(l):
    sum=0
    for i in l:
        sum+=i
    return sum
        
l=[2,4,6,8]
print(sum_list(l))




# Q12. Reverse a String

# Create a function that accepts a
# string and returns its reverse.
# Example:
# Input:
# Python
# Output:
# nohtyP

# Solution :-

def rev(s):
    l=list(s)

    left = 0
    right=len(l)-1
    while left< right:
        l[left],l[right] = l[right],l[left]
        left=left+1
        right-=1
        return "".join(l)
   
    
s=input("Enter a String : ")
result=rev(s)
print(result)
if(rev(s)==(s)):
    print("Valid ")
else:
    print("invalid")  



      


     


    
    