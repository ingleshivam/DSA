arr = [3,1,2,4,1,5,2,6,4]

def merge_array(left_array, right_array):
    i=j=0
    m,n = len(left_array), len(right_array)
    result = []
    while i<m and j<n:
        if left_array[i] <= right_array[j]:
            result.append(left_array[i])
            i+=1
        else:
            result.append(right_array[j])
            j+=1
    if i<=m:
        while i<m:
            result.append(left_array[i])
            i+=1
    if j<=n:
        while j<n:
            result.append(right_array[j])
            j+=1
    
    return result
    
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left_array = arr[:mid]
    right_array = arr[mid:]
    left = merge_sort(left_array)
    right = merge_sort(right_array)
    return merge_array(left, right)

sorted_array = merge_sort(arr)
print("Sorted Array : ", sorted_array)