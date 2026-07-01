# validParenthisis.py

def isValid(selt, s:str) -> bool:
	validBrackets = {
		')': '(',
		']': '[',
		'}': '{'
	}
	brackets = []
	
	for item in s:
		if item in validBrackets.values():
			validBrackets.append(item)
		else:
			if not brackets or brackets.pop() != validBrackets[item]:
				return False
	return len(brackets) == 0