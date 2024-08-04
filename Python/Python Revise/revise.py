'''Taking user input'''

name = input("Please enter your name: ")

print("Nice to meet you ", name)

'''Type Casting'''

num_int = 13
num_float = 13.1
num_str = "123"
new_num = num_int + num_float

print("The datatype of num_int is ",type(num_int))
print("The datatype of num_float is ",type(num_float))
print(num_float)
print("The datatype of new_num is ",type(new_num))
print(num_int + int(num_str))

'''Swapping Values'''
a = 10
b = 20
print(a, b)

a, b = b, a
print(a, b)

'''String'''
a = "Hello World"
print(a)
print(0)
print(a[-1])
print(a[0:3])
print(a[0:])
print(a[1:])
print(a[:4])
print(a[0:-1])

'''Math Functions'''
import math
x = float(input("Please enter a decimal number "))
print(x)
print(round(x))
print(abs(-x))
print(math.ceil(x))
print(math.floor(x))

'''If Else Statement'''
i = int(input("Please enter a number: "))

if i > 15:
    print("i is greater than 15")
    print("I'm in if block")

else:
    print("i is less than 15")
    print("I'm in else block")

print("I'm not in if else block")

i = 20
if i == 10:
    print("i is 10")

elif i == 15:
    print("i is 15")

elif i == 20:
    print("i is 20")

else:
    print("i is not present")

'''Logical operators'''
a = 10
b = -10
c = 0

if a>0 or b>0:
    print("Either of the number is 0")

else:
    print("None of the number is o")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if not a%3 == 0 or a%5 == 0:
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")


'''Ternary Operators'''
num1 = 15
num2 = 20

if num1>num2:
    print(num1)

else:
    print(num2)

print(num1 if num1>num2 else num2)

'''While Loop'''
i = 1

while i < 6:
    print(i)

    if i==3:
        break
    i += 1

while i < 6:
    i += 1

    if i==3:
        continue
    print(i)

n = int(input("Please enter a number: "))
sum = 0
i = 1

while i <= n:
    sum +=i
    i += 1

print(sum)

'''For Loop'''
for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

num = [1,2,3,4,5]
for x in num:
    print(x)


for x in range(6):
    print(x)

for x in range(2,6):
    print(x)

for x in range(2,30,3):
    print(x)

adj = ["red","big","tasty"]
fruit = ["apple","banana","cherry"]
for x in adj:
    for y in fruit:
        print(x,y)

'''List'''
ThisList = ["apple","banana","cherry"]
print(ThisList)

list1 = ["Apple", "Banaba", "Cherry", "Mango", "Guava"]
print(list1[0:2])
print(list1[2:])
print(list1[-1])
print(list1[-3:-1])
print(list1[0:5])
print(list1[0:5:2])
print(list1[-1:-2])
print(list1[-1:-2:-1])

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
list5 = ["apple"]
string1 = "apple"
print(list1[0])
print(string1[0])

list1 = ["Apple", "Banaba", "Cherry", "Mango", "Orange"]
print(list1+["Tomato",50])
print(list1*3)
print(list1)

input_string = input("Please enter numbers seperated by space: ")
list = input_string.split()
print("Calculating the sum of the elements of the input list")
sum = 0

for num in list:
    sum += int(num)
print("Sum = ", sum)

'''Tuple'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

'''Set'''
# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
my_set = set([1, 2, 3, 2])
print(my_set)

num1 ={1, 2, 3, 4, 5}
num2 ={4, 5, 6, 7}

print(num1 | num2)   #union
print(num1 & num2)   #intersection
print(num1 - num2)   #difference

'''Dictionary'''
thsdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thsdict)
print(thsdict["brand"])
print(thsdict.get("Name","Invalid Key"))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)



'''Array'''
A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column = []        # empty list
for row in A:
  column.append(row[2])   

print("3rd column =", column)

'''Functions'''
def my_function(fname):
    print("Name: " +fname)

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
      print(fname + " " + lname)

my_function("Emil", "Refsnes")

def my_function(child3, child2, child1):
      print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(country = "Norway"):
      print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def Add(a, b):
    '''
    This will take two parameter
    Return value is integer
    '''
    return a + b

print(Add(10, 20))
print(Add.__doc__)

x = lambda a : a + 10
print(x(5))

sum = lambda x, y, z : x + y + z
print(sum(1,2,3))

cube = lambda y: y*y*y
print(cube(2))

def my_func(a):
    return len(a)

x = list(map(my_func,("apple","banana","cherry")))
print(x)

def square(x):
    return x*x

num = list(map(square,(1,2,3,4,5)))
print(num)

ages = [5, 12, 17, 18, 24, 32]

def my_f(a):
    if a < 18:
        return False
    
    else:
        return True

adults = list(filter(my_f,ages))
print(adults)
    
num = [5, 12, 17, 18, 25, 32]

result = list(filter(lambda a : a%2 == 0,num))
print(result)
print(num)

'''Class'''
class student:
    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa =  gpa
    def display(self):
        print(f"Roll = {self.roll},GPA = {self.gpa}")

kamal = student()
kamal.set_value(10, 3.75)
kamal.display()

class stud1:
    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll = {self.roll}, GPA = {self.gpa}")

jamal = stud1(1,4)
jamal.display()

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def disp(self):
        print(f"First name  = {self.fname}, Last name = {self.lname}")

a = person("Rahim", "Uddin")
a.disp()

class stu(person):
    pass
    def section(self, sec):
        self.sec = sec
    def display(self):
        print(f"Section = {self.sec}")        
    
b = stu("Abul", "Hasan")
b.disp()
b.section("A")
b.display()

'''Inheritance to advance'''

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print("First name: ", self.fname, " Last name: ", self.lname)

class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.fname, self.lname, " to the class of ", self.graduationyear)
    
c = student("Mike", "Olsen", 2019)
c.display()
c.welcome()
        