arr = [5,7,8,4,1,6,9,2]

def selectionSort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index] :
                min_index = j
        arr[i], arr[min_index] = arr[min_index],arr[i] 
    return arr

sorted_array = selectionSort(arr)
print("Sorted Array : ", sorted_array)