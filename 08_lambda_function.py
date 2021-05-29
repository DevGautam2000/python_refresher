"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 6:49 PM

"""

# one way of doing it
print((lambda x, y: x + y)(5, 6))


# modular approach
def doubled(x):
    return x * 2


singles = [1, 2, 3, 4, 5, 6]
doubles = [doubled(x) for x in singles]
print(doubles)

# using lambda functions
doubles = [(lambda x: x * 2)(x) for x in singles]
print(doubles)

# using lambda function along with map function
doubles = map(lambda x: x * 2,
              doubles)  # to print we need to change the returned value as list as map returns an generator object
print(list(doubles))
