"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 2:15 AM

"""

# sequence
friends = [
    {"name": "Gautam Chandra Saha", "age": 21},
    {"name": "Rishabh Prasad", "age": 21},
    {"name": "Adittya Prasad", "age": 20},
    {"name": "Samyak Mehta", "age": 21}
]

expected = "Gautam Prasad"


def get_friend_name(friend):
    return friend["name"]


def search(sequence, expected_ele, finder_func):
    for friends in sequence:
        if finder_func(friends) == expected_ele:
            return print(f"{expected_ele} is found.")

    print(f"{expected_ele} is not found.")


if __name__ == '__main__':
    search(friends, expected, get_friend_name)
