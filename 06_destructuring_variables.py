"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 5:15 PM

"""

print("_____________destructuring a tuple_______________")
# destructuring a variable from a tuple
tuplee = "Gautam", 21
person, age = tuplee
print(f"{person} is {age} years old.")

dict = {
    "Gautam": 21,
    "Rishabh": 21,
    "Adittya": 20
}
print("_____________destructuring a dictionary_______________")
# destructuring a variable from a dictionary
for name, age in dict.items():
    print(f"{name} is {age} years old.")

print("_______________________________________")
friends = [key for key in dict.items()]
print(friends)
print("_______________________________________")

print("___________destructuring a list using *____________")
listt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *rest = listt
print(first)
print(rest)

print("_______________________________________")
*most, last = listt
print(most)
print(last)
