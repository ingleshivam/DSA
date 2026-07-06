# countEvenOdd.py

from collections import Counter

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

counts = Counter(['even' if num % 2 == 0 else 'odd' for num in a])

print("Even numbers:", counts['even'])
print("Odd numbers:", counts['odd'])