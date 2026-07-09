# firstNonRepeating.py

def first_non_repeating(s):
    counts = {}

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in s:
        if counts[ch] == 1:
            return ch

    return None


print(first_non_repeating("aabbcdde"))  
print(first_non_repeating("aabbcc"))    
print(first_non_repeating("leetcode"))  
print(first_non_repeating("loveleetcode")) 