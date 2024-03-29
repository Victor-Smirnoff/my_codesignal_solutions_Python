# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/KLbRMcWhaZi3dvYH5
# Increase Number Roundness
# Define an integer's roundness as the number of trailing zeroes in it.
# Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.
# Example
# For n = 902200100, the output should be solution(n) = true.
# One of the possible ways to increase roundness of n is to swap digit 1 with digit 0 preceding it: roundness of 902201000 is 3, and roundness of n is 2.
# For instance, one may swap the leftmost 0 with 1.
# For n = 11000, the output should be solution(n) = false.
# Roundness of n is 3, and there is no way to increase it.

def solution(n):
    res = []
    count = 0
    n = str(n)
    for i in range(len(n)):
        if n[i] == '0':
            count += 1
            continue
        else:
            if count != 0:
                res.append(count)
                count = 0
            else:
                continue

    return True if len(res) > 0 else False
