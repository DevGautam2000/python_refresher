"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 1:42 PM

"""
import functools

# suppose we have user access permission for a router
user = {"username": "Gautam", "access": "admin"}


# to secure the password from unauthorized access we need a decorator
def make_secure_fetch(func):
    @functools.wraps(func)
    def secured_password(*args, **kwargs):

        if user["access"] in ("admin", "user", "billing"):
            val = func(*args, **kwargs)
            if val is None:
                return f"{user['username']} has no access to the network."
            else:
                return val

    return secured_password


# set a method that fetches password for the user if admin
@make_secure_fetch
def get_pass(access_level):  # now the function only gets invoked if the decorator function is generated
    if "admin" in access_level:
        return "1234"

    elif "user" in access_level:
        return "user_password"


@make_secure_fetch
def get_billing_pass():
    if user["access"] == "billing":
        return "billing_pass"


def main():
    # wrapper gives the original function name
    print(get_pass.__name__)  # --> gives secure_password but after using functools
    print(get_pass(user["access"]))
    print(get_billing_pass())


if __name__ == '__main__':
    main()
