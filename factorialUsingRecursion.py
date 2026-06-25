n = 5
num = n

def factorialOfNumber(num):
    if num ==1:
        return 1
    return num * factorialOfNumber(num-1)

result = factorialOfNumber(num)
print("Result : ", result)