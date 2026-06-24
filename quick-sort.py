arr = [4, 1, 3, 9, 7]

def quickSort(arr, low, high):
    if low<high:
        p_index = partition(arr, low, high)
        quickSort(arr, low, p_index-1)
        quickSort(arr, p_index+1,high)
        
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    
    while i<j:
        while arr[i] <=pivot and i<=high-1:
            i+=1 
        
        while arr[j] >=pivot and j>=low+1:
            j-=1
    
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    
    return j

quickSort(arr,0,len(arr)-1)
print(arr)