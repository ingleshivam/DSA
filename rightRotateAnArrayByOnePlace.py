# rightRotateAnArrayByOnePlace.py


# #Using Slicing
# arr = [5, -2, 3,9, 0, 6,10,7]
# def rightRotateAnArrayByOnePlace(arr):
#     length = len(arr)-1
#     arr[:] = [arr[-1]] + arr[0:length]
#     return arr
# result = rightRotateAnArrayByOnePlace(arr)
# print("Result : ", result)

#Using Looping
arr = [5, -2, 3,9, 0, 6,10,7]
def rightRotateAnArrayByOnePlace(arr):
    length = len(arr)
    # k = arr[length-1]
    n = 3
    while n > 0:
        k = arr[length-1]
        for i in range(length-2,-1,-1):
            arr[i+1] = arr[i]
        arr[0] = k
        n-=1
    return arr 

result = rightRotateAnArrayByOnePlace(arr)
print("Result : ", result)