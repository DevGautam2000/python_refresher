"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 9:36 PM

"""


class Store:

    def __init__(self):
        self.name = ""
        self.items = []

    def add_item(self, name, price):
        items = {"name": name, "price": price}
        self.items.append(items)

    def get_price_all(self):
        return sum([item["price"] for item in self.items])


def main():
    s = Store()
    s.add_item("Bat", 100)
    s.add_item("Ball", 200)
    s.add_item("Badminton", 300)
    s.add_item("Shuttle Cock", 400)

    print(s.get_price_all())


if __name__ == '__main__':
    main()
