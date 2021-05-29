"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 12:11 AM

"""


class Guitar:
    TYPES = ("Stratocaster", "Les Paul")

    def __init__(self, customer_name: str, guitar_type: str, address: str):
        self.customer_name = customer_name
        self.guitar_type = guitar_type
        self.address = address
        self.instance_method()

    def instance_method(self):
        print(f"Welcome, {self.customer_name}")

    @classmethod
    def stratocaster(cls, customer_name: str, address: str) -> "Guitar":
        return cls(customer_name, cls.TYPES[0], address)

    @classmethod
    def les_paul(cls, customer_name: str, address: str) -> "Guitar":
        return cls(customer_name, cls.TYPES[1], address)

    @staticmethod
    def static_method() -> str:
        return "Hurray!"

    def __str__(self) -> str:
        return f"{self.customer_name} your booking for {self.guitar_type} is confirmed! {Guitar.static_method()}"


def main():
    cust1 = Guitar.stratocaster("Gautam", "Gangtok")
    print(cust1)

    cust2 = Guitar.les_paul("Rishabh", "Siliguri")
    print(cust2)


if __name__ == '__main__':
    main()
