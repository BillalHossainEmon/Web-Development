'''Single Inheritance'''

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def display(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.display()


class Student(Person):
    pass

y = Student("Abul", "Hossain")
y.display()

'''Multiple Inheritance'''

class A:
    def display1(self):
        print("This is class A")

class B:
    def display2(self):
        print("This is class B")

class C(A,B):
    def display3(self):
        print("This is class C")

objC = C()
objC.display1()
objC.display2()
objC.display3()

'''Multi Level Inheritance'''

class A:
    def display1(self):
        print("This is class A")

class B(A):
    def display2(self):
        print("This is class B")

class C(B):
    def display3(self):
        print("This is class C")

objctC = C()
objctC.display1()
objctC.display2()
objctC.display3()

'''Hierarchical Inheritance'''

class ParentClass:
    def func1(self):
        print("This function is in parent class")

class Child1(ParentClass):
    def func2(self):
        print("This function is in First Child class")

class Child2(ParentClass):
    def func3(self):
        print("This function is in Second Child class")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
