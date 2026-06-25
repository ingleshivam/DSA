# Count the number of digits in an integer.

n = 58733112
num = n

def countNumberOfDigits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

print(countNumberOfDigits(num))