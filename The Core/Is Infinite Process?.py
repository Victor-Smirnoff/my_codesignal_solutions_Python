# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/aFF9HDm2Rsti9j5kc
# Is Infinite Process?
# Given integers a and b, determine whether the following pseudocode results in an infinite loop
# while a is not equal to b do
#   increase a by 1
#   decrease b by 1
# Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.
# Example
# For a = 2 and b = 6, the output should be
# solution(a, b) = false;
# For a = 2 and b = 3, the output should be
# solution(a, b) = true.

def solution(a, b):
    if a > b:
        return True
    if (b - a) % 2 != 0:
        return True
    return False
