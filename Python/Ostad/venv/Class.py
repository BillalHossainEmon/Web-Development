class student1():
    roll = ""
    gpa = ""

kamal = student1()
kamal.roll = 10
kamal.gpa = 3.75

print(f"Roll = {kamal.roll}, GPA = {kamal.gpa}")

class student2:
    def set_val(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll = {self.roll}, GPA = {self.gpa}")


Jamal = student2()
Jamal.set_val(11,3.5)
Jamal.display()

class student3:
    def __init__(self):
        self.section = "A"
    def display(self):
        print(f"Section = {self.section}")

kamal = student3()
kamal.display()

class student4:
    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll = {self.roll}, GPA = {self.gpa}")

Rahim = student4(1, 4.0)
Rahim.display()