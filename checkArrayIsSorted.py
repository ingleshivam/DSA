# checkArrayIsSorted.py

arr = [1 ,2, 3, 5, 5, 7, 7, 7, 8, 12, 13, 15, 15, 15, 19]

def checkArrayIsSortedInAscendingOrder(arr):
    isSorted = False
    for i in range(0,len(arr)-1):
        if arr[i] <= arr[i+1]:
            continue
        else:
            return isSorted
    isSorted  = True
    return isSorted

result = checkArrayIsSortedInAscendingOrder(arr)
print(result)