print('Hello World')

num = 2

print('The number is', num, 'and it is an even number'  )

inp = input('Enter a number: ')

print('You entered', inp)

if 1 > 2:
    print('5 is greater than 2')
else:
    print('5 is less than 2')

x, y, z = "Orange", "Banana", "Apple"

print(x)

print(y)

print(z)

print(x + y + z)

xy = 'awesome'

def myfunc():
    yz = 'I am'
    print('Python is ',xy)
    print(yz, xy)

myfunc()

thislist = ["Orange", "Banana", "Apple"]

print(thislist)

print(thislist[1])

thislist[1] = "Lemon"

print(thislist)

thislist.append("Banana")

print(thislist)

thislist.insert(1, "Cherry")

print(thislist)

tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)

for x in thislist:
    print(x)