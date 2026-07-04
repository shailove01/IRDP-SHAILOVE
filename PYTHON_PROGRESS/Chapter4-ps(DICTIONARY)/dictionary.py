names = {
    "rohan" : 100,
    "ram" : 120,
    "shyam" : 420,
    "fruits" : ["Aam", "Kela", "etc."]
    }
print(names.items())  #  prints all the items 
print(names.keys())   #  prints the key elements of the dictionary. i.e. returns all the keys .

print(names.values())  #  prints the values of the dictionary.
names.update({"rohan" : 120})  # Updates existing values or adds new one.
print(names)

print(names.get("ram"))
names.pop("ram")   # Removes a key .
print(names)

names.popitem()   # Removes the last inserted items from the dictionary .
print(names)

names.clear()    #  Removes everything i.e clears the entire table .
print(names)


new_names =names.copy()   # Creates a copy of the original table .
print(new_names)

names.setdefault("ram", 120)
print(names)

