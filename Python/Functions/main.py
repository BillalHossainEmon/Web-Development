def my_function(fname):
    print("Hello my name is " + fname)

print(my_function("Emil"))


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

x = lambda a, b, c : a + b + c
print(x(1,2,3))

def cube(y):
    return y*y*y

print(cube(5))

lambda_cube = lambda y : y * y * y
print(lambda_cube(5))

def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))

def square(x):
    return x*x

num = [1,2,3,4,5]

result = list(map(square, num))

print(result)

def cube(x):
    return x*x*x

num = [1,2,3,4,5]

result = list(map(cube,num))

print(result)

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = list(filter(myFunc, ages))

print(adults)


num = [5, 12, 17, 18, 25, 32]

result = list(filter(lambda x : x%2==0,num))

print(result)