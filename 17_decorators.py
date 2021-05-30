"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 1:02 PM

"""

# suppose we have user access permission for a router
user = {"username": "Gautam", "access": "guest"}


# set a method that fetches password for the user if admin
def get_user_pass():
    return "1234"


# to secure the password from unauthorized access we need a decorator
def make_secure_fetch(func):
    def secured_password():
        if user["access"] == "admin":
            return func()
        else:
            return f"{user['username']} has no access to the network."

    return secured_password


get_user_pass = make_secure_fetch(get_user_pass)

print(get_user_pass())

"""
    hence make_secure_fetch is the decorator function
    But this code has a problem
    TODO --> resolve code in 18_decorators(resolved).py

"""
