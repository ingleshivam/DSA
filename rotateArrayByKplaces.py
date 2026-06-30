#rotateArrayByKplaces.py

arr= [1,2,3,4,5,6,7]
k = 3

def rotateArrayByKPlace(arr,k):
    length = len(arr)
    k%=length
    arr[:] = arr[length-k:] + arr[:length-k]

result = rotateArrayByKPlace(arr, k)
print("Final Result Array : ",arr)