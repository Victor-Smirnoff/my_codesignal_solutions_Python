# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32

# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# solution(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".

def solution(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    count = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            count += 1
            s2.remove(s1[i])
    return count
