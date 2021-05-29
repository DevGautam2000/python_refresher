"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 3:33 PM

"""

friends = ["Gautam", "Rishabh"]
friends_copy = ["Gautam", "Rishabh"]

print(friends == friends_copy)
print(friends is friends_copy)  # returns false as each list created in memory is assigned a different address
