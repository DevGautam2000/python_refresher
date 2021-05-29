"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 11:45 PM

"""


class Shelf:

    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Capacity of shelf: {len(self.books)}"

    def get_books(self):
        return [book.name for book in self.books]


class Books:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book name: {self.name}"


def main():
    book1 = Books("Harry Porter")
    book2 = Books("Cars")
    book3 = Books("Time Machine")

    shelf = Shelf(book1, book2, book3)

    print(shelf)
    print(f"Books are: {shelf.get_books()}")


if __name__ == '__main__':
    main()
