"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 9:16 PM

"""


class Student:

    def __init__(self, name, *grade_args):
        self.name = name
        self.grades = list(map(lambda x: x, *grade_args))

    def avg(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"[Name: {self.name},Average Score: {round(self.avg(), 2)}]"

    def __repr__(self):  # more useful when debugging
        return f"<{__class__} Name: {self.name}, Average Score: {round(self.avg(), 2)}>"


def main():
    print("CONCEPTS OF OOP")

    # create a Student object
    student1 = Student("Gautam", (90, 100, 75, 80))
    student2 = Student("Rishabh", (100, 100, 75))

    print(student1)
    print(student2.__repr__())


if __name__ == "__main__":
    main()
