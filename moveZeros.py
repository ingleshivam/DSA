# moveZeros.py

def moveZeros(arr):
    n = len(arr)
    i = 0
    j = 1
    while j<n:
        if arr[i] == 0 and arr[j] !=0:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j+=1
        else:
            j+=1
arr = [1,2,0,4,3,0,0,3,5,1]
moveZeros(arr)
print(arr)
    