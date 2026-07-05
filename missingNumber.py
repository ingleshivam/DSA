# missingNumber.py

arr = [9,6,4,2,3,5,7,0,1]

def findMissingNumber(arr):
    length = len(arr)
    ExpectedSum = 0
    ActualSum = 0
    for i in range(length):
        ExpectedSum = ExpectedSum + i + 1
        ActualSum = ActualSum + arr[i]
    return ExpectedSum - ActualSum
output  = findMissingNumber(arr)
print(output)