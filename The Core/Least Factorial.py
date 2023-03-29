# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/7BFPq6TpsNjzgcpXy
# Least Factorial
# Given an integer n, find the minimal k such that
# k = m! (where m! = 1 * 2 * ... * m) for some integer m;
# k >= n.
# In other words, find the smallest factorial which is not less than n.
# Example
# For n = 17, the output should be solution(n) = 24.
# 17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).

from math import factorial

def solution(n):
    tmp = 0
    num = 1
    while tmp < n:
        tmp = factorial(num)
        num += 1

    return tmp
