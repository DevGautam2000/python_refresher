"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 1:13 PM

"""
import functools

"""
    The problem in the code is that 
    
    1. even if the function get_user_pass is secured after the decorator function but a call to it 
    before the decorator function hinders the security of the code. Hence, to handle that we need to use annotations
    
    2. Python internally sets the name of the calling function with the newly defined function inside 
    of the decorator function and hence that can be cumbersome.Hence, to handle that we nedd to use functools module
    to wrap the calling function 

"""

# suppose we have user access permission for a router
user = {"username": "Gautam", "access": "guest"}


# to secure the password from unauthorized access we need a decorator
def make_secure_fetch(func):
    @functools.wraps(func)
    def secured_password():
        if user["access"] == "admin":
            return func()
        else:
            return f"{user['username']} has no access to the network."

    return secured_password


# set a method that fetches password for the user if admin
@make_secure_fetch
def get_user_pass():  # now the function only gets invoked if the decorator function is generated
    return "1234"


def main():
    # wrapper gives the original function name
    print(get_user_pass.__name__)  # --> gives secure_password but after using functools
    print(get_user_pass())


if __name__ == '__main__':
    main()
