n = 8
num = n 
def fibonacci(num):
    if num == 0 or num ==1:
        return num

    return fibonacci(num-1) + fibonacci(num-2)
    
result = fibonacci(num)
print("Result : ", result)