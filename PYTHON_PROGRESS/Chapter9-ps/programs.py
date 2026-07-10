
class Employee:
    a=1
class Shailove(Employee):    # Single Level Inheritance occured.
    b=2
class Coder(Shailove):       # Multi- Level Inheritance occured.
    c=3

o = Employee()
print(o.a)     #Prints the a attribute
o = Shailove()
print(o.a,o.b)    # Child Class of Employee Class.
o = Coder()
print(o.a, o.b, o.c)    #Child Class of both Employee and Shailove Class.
                            # Multi-Level Inheritence Occured



