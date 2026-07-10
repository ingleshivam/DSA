def findTargetElementUsingLinearSearch(arr, target):
    for num in arr:
        if num == target:
            print(f"Target element found at position {arr.index(num)}")
arr = [5,3,9,8,1,6,4,-10,-100]
target = 4

position = findTargetElementUsingLinearSearch(arr, target)