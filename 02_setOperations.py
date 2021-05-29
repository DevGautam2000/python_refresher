"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 3:06 PM

"""

friends = {"Gautam", "Qazi", "Rishabh"}

friends_abroad = {"Qazi", "Rishabh"}
friends_local = friends.difference(friends_abroad)

print(f"Local friends: {friends_local}")
print(f"Total friends: {friends_local.union(friends_abroad)}")

studied_together = friends.intersection(friends_abroad)
print(f"Studied together: {studied_together}")

print(f"friends_local is a subset of friends: {friends_local.issubset(friends)}")
print(friends.symmetric_difference(friends_abroad))  # gives a difference for finding difference from any set to any
# set unlike the difference method

friends.add("Adittya")

print(friends)

s1 = {1, 2, 4, 5, 8, }
s2 = {5, 8}

print(s2.difference(s1))
