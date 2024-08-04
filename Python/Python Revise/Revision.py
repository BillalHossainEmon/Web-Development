new = input("Enter your name: ")
print("Hello: ",new)

a = 10
b = 20

a,b = b, a
print(a,b)

a = "Hello world"

print(a)
print(a[-1])
print(a[0:-1])

a = int(input("Please enter a number: "))

if a > 15:
    print("a is greater than 15")

elif a > 10:
    print("a is greater than 10")

else:
    print("a is not greater than 10 or 15")


i = 1
while i<6:
    print(i)
    i += 1


i = 1
while i<6:
    print(i)
    if i==3:
        break
    i += 1

i = 1
while i<6:
    print(i)
    if i==3:
        continue
    i += 1


