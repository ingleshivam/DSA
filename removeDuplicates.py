# removeDuplicates.py
arr = [0,0,1,1,1,2,2,3,3,4]
def removeDuplicates(arr):
    i = 0
    j = 1
    length = len(arr)
    while j < length:
        if arr[i] == arr[j]:
            j+=1
        else:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]        
            j+=1
    return i+1
        
removeDuplicates(arr)