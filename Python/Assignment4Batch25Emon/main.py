def AscendingSort(l):

    AscendingList = []

    for x in l:

            AscendingList.append(x)

    AscendingList.sort()

    return AscendingList

List = [1, 5, 2, 9, 3, 22, 13]

print(List)

print(AscendingSort(List))