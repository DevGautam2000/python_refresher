"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 8:04 PM

"""


def k_args(*args, **kwargs):
    pretty(True, *args, **kwargs)


def pretty(is_pretty, *args, **kwargs):
    if is_pretty:
        print({
            "Positional args": args,
            "Keyword args": kwargs
        })

    else:
        print(args)
        print(kwargs)


# this is how to pass both args and kwargs using a single function
val_dict = {"name": "Gautam", "age": 21}
k_args(1, 2, 3, **val_dict)
pretty(False, 4, 5, 6, name="Rishabh", hobby="coding")
