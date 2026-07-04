items = ["apple", "aaloo", "pyaaj",0.19, False, "yoyo"]
nums = [1,5,8,6,2,3]
print(items[5])
items[5] = "jiyaan"   # this shows that lists are mutable. 
print(items)

items.append("Honey Singh")  #  .append method adds the given data or item at the last of the list.
print(items)
items.reverse()  # reverses the whole list from right to left .
print(items)
items.pop(4)   # removes items based on the indexes. note: pop() will only work with indexes not the item names or anything .
print(items)
nums.sort()  # Does sorting according to the condition defined . if the condition is not mentioned then it will follow the basic ascending order sorting principle.
print(nums)
items.remove("Honey Singh")   # this .remove() method is not like .pop() method . this method removes elements by their names without needing any indexing or index numbers.
print(items)
items.insert(3,"KI AAL HAI JI ?")   # .insert() method helps users in inserting the values at any places or index accross the list .
print(items)   
