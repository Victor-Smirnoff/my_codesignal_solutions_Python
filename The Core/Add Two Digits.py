# https://app.codesignal.com/arcade/code-arcade/intro-gates/wAGdN6FMPkx7WBq66
# Add Two Digits
# You are given a two-digit integer n. Return the sum of its digits.
# Example
# For n = 29, the output should be
# solution(n) = 11.

def solution(n):
    return n // 10 + n % 10
