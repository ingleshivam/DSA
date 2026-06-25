# Print all factors of a given number
n = 20
num  = n

def printFactorsOfNumbers(num):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result

result  = printFactorsOfNumbers(num)
print(result)