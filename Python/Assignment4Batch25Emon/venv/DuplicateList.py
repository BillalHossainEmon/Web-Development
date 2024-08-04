List1 = [1,5,6,5,5,1,2,3]
List2 = []
DuplicateList = []

print(List1)

for x in List1:
    if x not in List2:
        List2.append(x)
    else:
        DuplicateList.append(x)

print(DuplicateList)