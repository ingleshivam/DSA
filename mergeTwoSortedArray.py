# mergeTwoSortedArray.py

# nums1 = [1,1,1,2,4,6,7]
# nums2 = [1,2,3,6,7,8,9,10]

nums1 = [2 ,2, 4, 6, 6, 8]
nums2 = [4 ,4 ,6]

# nums1 =[1, 1, 1, 1, 1]
# nums2 = [2, 2, 2, 2, 2]

def mergeTwoSortedArray(left, right):
    i=j=0
    n,m = len(left), len(right)
    result = []
    while i < n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i < n:
        while i<n:
            result.append(left[i])
            i+=1
    
    if j < m:
        while j < m :
            result.append(right[j])
            j+=1
        
    sorted_array =list(set(result))
    sorted_array.sort()
    return sorted_array

result = mergeTwoSortedArray(nums1,nums2)
print("Result Array : ", result)