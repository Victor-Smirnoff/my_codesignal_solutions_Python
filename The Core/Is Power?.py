# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/yBFfNv5fTqhcacZ7w
# Is Power?
# Determine if the given number is a power of some non-negative integer.
# Example
# For n = 125, the output should be solution(n) = true;
# For n = 72, the output should be solution(n) = false.

def solution(n):
    for a in range(1, 400):
        for b in range(2, 10):
            if a ** b == n:
                return True
    return False
