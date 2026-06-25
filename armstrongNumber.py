# Armstrong number

n = 153
num = n 
def armstrongNumber(num):
    sum = 0
    while num > 0:
        rem  = num % 10
        sum  = sum + rem**3
        num = num // 10
    return sum

if num == armstrongNumber(num):
    print("The number is Armstrong number")
else:
    print("The number is not Armstrong number")