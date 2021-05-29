"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 12:55 AM

"""

from libs import __lib__


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


if __name__ == '__operations__':
    print("Imported from operations")
    print(__lib__.main())
    print(f"operations.py: {__name__}")
