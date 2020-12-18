# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".

from collections import Counter
# Import collections from Counter
def commonCharacterCount(s1, s2):
    # Define counter - Works similar to a dictionary
    c1 = Counter(s1)
    c2 = Counter(s2)
    # Use sum function
    sum_ = 0
    seen = set()
    # Loop through s1
    for c in s1:
        if c in c2 and c not in seen:
            sum_ += c2[c] if c1[c] > c2[c] else c1[c]
            seen.add(c)
    return sum_

