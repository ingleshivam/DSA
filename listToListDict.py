# listToListDict.py

a = ["name", "age", "city"]  
b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]] 

ans = [dict(zip(a, values)) for values in b]

print(ans)