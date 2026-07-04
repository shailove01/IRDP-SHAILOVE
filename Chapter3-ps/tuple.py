# Tuple is an ordered collection which can store multiple values  in one variable.

x= (10,50,55,69,89,0,3,4) 
y= (2,3,6,2,"meoowwwwww", "bagad billa")
# print(type(x))
# print(type(y))
# print(x.count(2))    # .count()  returns the number of how many times an element appears.
# print(y.count(8))

print(y.index("bagad billa"))   # .index() returns the index of the first occurence of an element.

print(len(x))  # len() is a built in python function which tells how many elements are there in the tuple.

print(max(x))   # max() is an python's built-in function that returns the maximum element across the tuple.

print(min(x))   # min() is a python's built-in function that returns the minimum element across the tuple .

print(sum(x))   # sum() returns the sum of all the elements across the tuple. Note :- It only works on the integer value elements .

print(sorted(x))   # sorted() returns the elements in either ascending order or descending order . Note:- It doesn't modify tuple, it returns a new list .

print(sorted(x, reverse=True))  # this will turn the sorting order to descending order.

