"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 1:56 AM

"""


class ReadTooManyPagesError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Book:

    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def read(self, pages_to_read):
        if pages_to_read > self.pages:
            raise ReadTooManyPagesError(f"The book {self.name} has only {self.pages} pages.")
        print(f"Read {pages_to_read} pages out of {self.pages} from {self.name}")


def main():
    truth = Book("Truth", 100)

    try:
        truth.read(50)
        truth.read(200)
    except Exception as err:
        print(f"ERROR: {err}")


if __name__ == '__main__':
    main()
