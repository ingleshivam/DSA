def getSecondOrderElements(n: int,  a):
    largest_number = second_largest_number = float("-inf")
    smallest_number = second_smallest_number = float("inf")
    for i in a:
        if i > largest_number:
            second_largest_number = largest_number
            largest_number = i 
        elif i < largest_number and i > second_largest_number:
            second_largest_number = i
        
        if i < smallest_number:
            second_smallest_number = smallest_number
            smallest_number = i
        elif i > smallest_number and i < second_smallest_number:
            second_smallest_number = i
        

    return [second_largest_number, second_smallest_number]

n = 4
a = [3,4,5,2]
print(getSecondOrderElements(n,a))