# https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico
# palindromeRearranging
# Given a string, find out if its characters can be rearranged to form a palindrome.
# Example
# For inputString = "aabb", the output should be solution(inputString) = true.
# We can rearrange "aabb" to make "abba", which is a palindrome.

def solution(inputString):
    set_inputString = set(inputString)
    inputString = list(inputString)
    res = 0
    for s in set_inputString:
        if inputString.count(s) % 2 != 0:
            res += 1

    return True if res <= 1 else False
