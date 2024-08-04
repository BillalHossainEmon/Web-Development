thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
list5 = ["apple"]
string1 = "apple"
print(list1[0])
print(string1[0])


list1 = ["Apple", "Banana", "Cherry", "Mango", "Guava"]

print(list1[0:2])
print(list1[2:])
print(list1[-1])
print(list1[-3:-1])
print(list1[0:5])
print(list1[0:5:2])
print(list1[-1:-2])
print(list1[-1:-2:-1])

list1 = ["apple", "banana", "cherry", "mango", "orange"]
print(list1 + ["tomato", 50])
print(list1 * 3)
print(list1)

list1 = ["apple", "banana", "cherry", "mango", "orange"]
list1[0] = "tomato"
print(list1)

input_string = input("Enter a list element in number separated by space: ")
list  = input_string.split()
print("Calculating sum of element of input list")
sum = 0
for num in list:
    sum += int (num)
print("Sum = ",sum)

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
