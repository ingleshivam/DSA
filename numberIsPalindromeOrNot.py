# Check if a number is palindrome or not

n = 12211
num = n  
def numberIsPalindromeOrNot(num):
    sum =0 
    while  num > 0:
        rem = num % 10
        sum = (sum * 10) + rem
        num = num // 10

    return sum

if n == numberIsPalindromeOrNot(num): 
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
