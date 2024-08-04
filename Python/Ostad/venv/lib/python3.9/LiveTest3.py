class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll_no = roll

    def Display(self):
        print(f"Name: {self.name}, Roll: {self.roll_no}")

obj = Student("John", 2)
obj.Display()