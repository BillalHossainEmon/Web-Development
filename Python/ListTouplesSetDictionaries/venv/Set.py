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
print(num2 - num1)   #difference