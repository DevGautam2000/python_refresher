"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 10:02 PM

"""


class Guitar:
    TYPES = ("Stratocaster", "Les Paul")

    def __init__(self, customer_name, guitar_type, address):
        self.customer_name = customer_name
        self.guitar_type = guitar_type
        self.address = address
        self.instance_method()

    def instance_method(self):
        print(f"Welcome, {self.customer_name}")

    @classmethod
    def stratocaster(cls, customer_name, address):
        return cls(customer_name, cls.TYPES[0], address)

    @classmethod
    def les_paul(cls, customer_name, address):
        return cls(customer_name, cls.TYPES[1], address)

    @staticmethod
    def static_method():
        return "Hurray!"

    def __str__(self):
        return f"{self.customer_name} your booking for {self.guitar_type} is confirmed! {self.static_method()}"


def main():
    cust1 = Guitar.stratocaster("Gautam", "Gangtok")
    print(cust1)

    cust2 = Guitar.les_paul("Rishabh", "Siliguri")
    print(cust2)


if __name__ == '__main__':
    main()
