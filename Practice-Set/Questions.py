'''
Level 1 - Question 1
Problem Statement
Ek e-commerce company apne products ki sales report generate kar rahi hai.
Har product ka sales count ek list mein diya gaya hai. Company chahti hai ki report mein second highest unique sales wala product identify kiya jaaye.
Agar sabhi products ki sales same hain ya sirf ek unique sales value exist karti hai, to report mein "No Second Highest Sales Found" display hona chahiye.
Example
Input
[120, 340, 560, 780, 560]
Output
560
Input
[500, 500, 500]
Output
No Second Highest Sales Found
Input
[-10, -30, -20]
Output
-20
Constraints
❌ sort() ya sorted() use nahi karna.
❌ List ko set mein convert nahi karna.
✅ Sirf ek traversal (O(n)) mein solution likhne ki koshish karo.
✅ Duplicate values ko sahi handle karo.
✅ Program har edge case handle kare.
Interviewer's Expectations
Main sirf output nahi dekhunga.
Main evaluate karunga:
Logic
Variable Naming
Readability
Edge Cases
Time Complexity
Space Complexity
Pythonic Coding Style
'''

x=[200,190,220,400,160,190,320]

highest = 0
sec_highest = 0
for i in x:

    if i > highest:
        sec_highest = highest
        highest = i

    elif(highest> i > sec_highest):
        sec_highest = i

if sec_highest == 0:
    print("No second Highest sales found.")

else :
    print(sec_highest)





# Level 1 - Question 2
# Problem Statement
# Ek e-commerce company ke warehouse mein products ke stock ki list di gayi hai.
# Manager ko sabse zyada stock ya second highest stock nahi chahiye.
# Usse sirf ye jaana hai ki warehouse mein kitni unique stock quantities hain.
# Example 1
# Input
# [10, 20, 20, 30, 10, 40]
# Output
# 4
# Unique stocks hain:
# 10, 20, 30, 40
# Example 2
# Input
# [5, 5, 5, 5]
# Output
# 1
# Example 3
# Input
# []
# Output
# 0
# 🚫 Constraints
# ❌ set() use nahi karna.
# ❌ collections.Counter use nahi karna.
# ❌ dict use nahi karna.
# ✅ Loops aur conditions ka use karna.
# ✅ Duplicates correctly handle hone chahiye.
       
def count_unique_stocks(self,stocks):
    self.stocks = stocks

    for i in stocks :
        i = 0
        i<=len(stocks)
        for j in stocks :
            if i
    







        
    




