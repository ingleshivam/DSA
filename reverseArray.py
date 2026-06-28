# reverseArray.py

def reverse(arr, left, right):
    if left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right-=1

arr = [3,9,5,6,7,2,10]
result = reverse(arr,0,len(arr)-1)
print("Reverse Array : ", arr)