"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 1:02 AM

"""


# from ..libs import __init__

def main():
    # print(__init__)  # gives an error as the main dir has no parent package
    return f"From {__name__}.py"


if __name__ == '__lib__':
    main()
