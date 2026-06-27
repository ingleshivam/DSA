def getSecondOrderElements(n,a):
    largest_number = second_largest_number = float("-inf")
    smallest_number = second_smallest_number = float("inf")

    for i in a:
        if i > largest_number:
            second_largest_number = largest_number
            largest_number = i
        elif largest_number > i and i > second_largest_number:
            second_largest_number = i
        
        if i < smallest_number:
            second_smallest_number = smallest_number
            smallest_number = i
        elif smallest_number < i and i < second_smallest_number:
            second_smallest_number = i

    return [second_largest_number, second_smallest_number]

print(getSecondOrderElements(5, [4,5,3,6,7]))