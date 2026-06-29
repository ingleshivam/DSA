#rotateArrayByKplaces.py

arr= [1,2,3,4,5,6,7]
k = 3

def rotateArrayByKPlace(arr,k):
    length = len(arr)
    arr[:] = arr[length-k:] + arr[:k+length]

result = rotateArrayByKPlace(arr, k)
print(arr)