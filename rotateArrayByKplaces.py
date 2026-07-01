#rotateArrayByKplaces.py

# arr= [1,2,3,4,5,6,7]
# k = 3

# def rotateArrayByKPlace(arr,k):
#     length = len(arr)
#     k%=length
#     arr[:] = arr[length-k:] + arr[:length-k]

# result = rotateArrayByKPlace(arr, k)
# print("Final Result Array : ",arr)

def rotateArrayByKPlace(arr,left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
arr= [1,2,3,4,5,6,7]
k = 3
n = len(arr)
print(n)
rotateArrayByKPlace(arr,n-k,n-1)
rotateArrayByKPlace(arr,0,n-1-k)
rotateArrayByKPlace(arr,0,n-1)

print(arr)
    