"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 12:15 AM

"""
from typing import List


class Shelf:

    def __init__(self, *books: List["Books"]):
        self.books = books

    def __str__(self) -> str:
        return f"Capacity of shelf: {len(self.books[0])}"

    def get_books(self) -> List:
        for books in self.books:
            return [book.name for book in books]


class Books:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Book name: {self.name}"


def main():
    book1 = Books("Harry Porter")
    book2 = Books("Cars")
    book3 = Books("Time Machine")
    book4 = Books("Journey To The Center Of The Earth")

    shelf = Shelf([book1, book2, book3, book4])

    print(shelf)
    print(f"Books are: {shelf.get_books()}")


if __name__ == '__main__':
    main()
