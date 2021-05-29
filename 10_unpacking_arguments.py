"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 7:35 PM

"""


def add(*args):
    total = 0
    for arg in args:
        total += arg

    return total


def mul(*args):
    total = 1
    for arg in args:
        total *= arg

    return total


def add1(x, y):
    return add(x, y)


val_set = {10, 20}
val_dict = {'x': 30, 'y': 20}
print(f"unpack using set: {add1(*val_set)}")  # unpacking argument from a set
print(f"unpack using dictionary: {add1(**val_dict)}")  # unpacking argument from a dictionary


def operate(*args, operator):
    if operator == "+":
        return add(*args)
    elif operator == "*":
        return mul(*args)


print("unpack using keyword arguments: ", end=' ')
print(operate(10, 20, operator="+"), end=' ')
print(operate(10, 2, operator="*"), end=' ')
