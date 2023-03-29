# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/hBw5BJiZ4LmXcy92u
# Count Sum of Two Representations 2
# Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.
# Example
# For n = 6, l = 2, and r = 4, the output should be solution(n, l, r) = 2.
# There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.

def solution(n, l, r):
    count = 0
    while l <= r:
        if l + r == n:
            count += 1
            l += 1
            r -= 1
        else:
            if l + r < n:
                l += 1
            else:
                r -= 1

    return count
