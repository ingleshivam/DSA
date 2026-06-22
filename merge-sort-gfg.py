# Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

# Examples:

# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# Explanation: We get the sorted array after using merge sort

arr =[4, 1, 3, 9, 7]
l = 0
r = 4

def merge(arr,l,r,mid):
    left_array = arr[l:mid+1]
    right_array = arr[mid+1:r+1]
    
    i=j=0
    m,n = len(left_array), len(right_array)
    k = l
    
    while i<m and j<n:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i+=1
        else:
            arr[k] = right_array[j]
            j+=1
        k+=1
    
    while i<m:
        arr[k] = left_array[i]
        i+=1
        k+=1
        
    while j<n:
        arr[k] = right_array[j]
        j+=1
        k+=1

def merge_sort(arr, l, r):
    if l>=r:
        return
    
    mid = (l+r)//2
    
    merge_sort(arr, l, mid)
    merge_sort(arr, mid+1, r)
    merge(arr, l, r, mid)
    
merge_sort(arr,l,r)
print("Sorted Array :", arr)
