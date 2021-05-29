"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 12:53 AM

"""

import __operations__
from libs import __lib__


def main():
    print(__operations__.add(5, 4))
    print(__operations__.mul(5, 4))
    print(__operations__.div(5, 4))

    # print(__operations__.__lib__.main())
    print(__lib__.main())  # though this gets printed but the module is imported only once


if __name__ == '__main__':
    print(f"import.py: {__name__}")
    main()
