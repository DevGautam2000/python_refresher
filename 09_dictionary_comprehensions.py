"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 7:13 PM

"""

users = {
    (0, "Gautam", "123456"),
    (1, "Rishabh", "123123"),
    (2, "Adittya", "456456")
}

# dictionary comprehension
_users = {user[1]: user for user in users}

username = "Gautam"
password = "12345"

# hence comprehending a dictionary can reduce boiler plate code
if password in _users[username]:
    print("User Authenticated")
else:
    print("User credentials does not match")
