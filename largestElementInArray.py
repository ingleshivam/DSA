arr = [55,32,-97,99,3,67]

def largestElementInAnArray(arr):
    largest = arr[0]
    for i in range(0,len(arr)):
        largest = max(largest, arr[i])
    return largest

print(largestElementInAnArray(arr))