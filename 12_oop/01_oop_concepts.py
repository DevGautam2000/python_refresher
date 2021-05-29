"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 8:55 PM

"""


class Student:

    def __init__(self, name, *grade_args):
        self.name = name
        self.grades = list(map(lambda x: x, *grade_args))

    def avg(self):
        return sum(self.grades) / len(self.grades)

    def display(self):
        print({
            "Name": self.name,
            "Average Score": round(self.avg(), 2)
        })


def main():
    print("CONCEPTS OF OOP")

    # create a Student object
    student1 = Student("Gautam", (90, 100, 75, 80))
    student2 = Student("Rishabh", (100, 100, 75))

    student1.display()
    student2.display()


if __name__ == "__main__":
    main()
