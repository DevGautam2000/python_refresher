"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 2:45 PM

"""

import functools

# suppose we have user access permission for a router
user = {"username": "Gautam", "access": "user"}


# to secure the password from unauthorized access we need a decorator
def make_secure_fetch(access_level):
    def decorator(func):
        # wrapper gives the original function name

        @functools.wraps(func)
        def secured_password():

            print(f"Name of calling function: {func.__name__}")
            if user["access"] == access_level:
                return func()
            else:
                return f"{user['username']} has no {access_level} access to the network.\n"

        return secured_password

    return decorator


# set a method that fetches password for the user if admin
@make_secure_fetch("admin")
def get_user_pass():  # now the function only gets invoked if the decorator function is generated
    return "admin_pass"


@make_secure_fetch("billing")
def get_billing_pass():
    return "billing_pass"


def main():
    print(get_user_pass())
    print(get_billing_pass())


if __name__ == '__main__':
    main()
