# REVERSE AN ARRAY USING RECURSION
n= [5,7,3,2,6,1,5,9]
# 9,5,1,6,2,3,7,5
num = n
i = 0
j = len(num)-1
def func(num,i,j):
    if i>=j:
        return
    num[i], num[j] = num[j],num[i]
    func(num,i+1,j-1)
    return num
print(func(num,i,j))