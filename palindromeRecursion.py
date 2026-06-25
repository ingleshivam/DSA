# Check if the string is palindrome or not using recursion

st = 'adsdfdsda'
s = st

l =0
r = len(s) - 1 

def func(s, l, r):
  
	if l==r or l>=r : 
		return True
	
	if s[l] == s[r]:
		return func(s,l+1,r-1)
	else:
		return False

print(func(s,l,r))