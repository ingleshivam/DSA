# moveZeros.py

def moveZeros(arr):
    n = len(arr)
    i = 0
    j = 0
    while i<n:
        if arr[i] == 0:
            j=i+1            
            while j < n and arr[j] == 0:
                j += 1
            if j<n:
                arr[i],arr[j] = arr[j], arr[i]
        i+=1    
                    
arr = [1,2,0,4,3,0,0,3,5,1]
moveZeros(arr)
print("Result Array : ",arr)


    