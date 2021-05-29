"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 6:20 PM

"""

defVal = 6


def add(x, y=3, z=defVal):
    print(x + y + z)


add(5, 6)

defVal = 5  # changing this has no effect as the param value is
# set ones the file is made
add(5, 6)
