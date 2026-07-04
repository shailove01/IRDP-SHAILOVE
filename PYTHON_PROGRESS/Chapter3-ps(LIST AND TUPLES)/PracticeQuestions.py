# 1:-  Write a program to store seven fruits name in the list .

# Solution:-

fruits=[]
a1= input("Enter the fruits name : ")
fruits.append(a1)
a2= input("Enter the fruits name : ")
fruits.append(a2)
a3= input("Enter the fruits name : ")
fruits.append(a3)
a4= input("Enter the fruits name : ")
fruits.append(a4)
a5= input("Enter the fruits name : ")
fruits.append(a5)
a6= input("Enter the fruits name : ")
fruits.append(a6)
a7= input("Enter the fruits name : ")
fruits.append(a7)

print(fruits)


# ____________________________________________________________________________

# 2:- Write a program to accept the marks of six students and display them in a sorted manner .
# 
# Solution:- 

students=[]
s1=input("1 :")
students.append(s1) 
s2=input("2 :")
students.append(s2) 
s3=input("3 :")
students.append(s3) 
s4=input("4 :")
students.append(s4) 
s5=input("5 :")
students.append(s5) 
s6=input("6 :")
students.append(s6) 

print(sorted(students, reverse=False))
