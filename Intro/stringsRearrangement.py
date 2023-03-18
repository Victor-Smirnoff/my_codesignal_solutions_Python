# https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9
# stringsRearrangement
# Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way 
# that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.
# Note: You're only rearranging the order of the strings, not the order of the letters within the strings!
# Example
# For inputArray = ["aba", "bbb", "bab"], the output should be
# solution(inputArray) = false.
# There are 6 possible arrangements for these strings:
# ["aba", "bbb", "bab"]
# ["aba", "bab", "bbb"]
# ["bbb", "aba", "bab"]
# ["bbb", "bab", "aba"]
# ["bab", "bbb", "aba"]
# ["bab", "aba", "bbb"]
# None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.
# For inputArray = ["ab", "bb", "aa"], the output should be
# solution(inputArray) = true.
# It's possible to arrange these strings in a way that each consecutive pair of strings 
# differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.

def solution(inputArray):
    def permutation(lst):
        if len(lst) == 0:
            return []
        if len(lst) == 1:
            return [lst]
        l = []
        for i in range(len(lst)):
            m = lst[i]
            remLst = lst[:i] + lst[i + 1:]
            for p in permutation(remLst):
                l.append([m] + p)
        return l

    def levenstein(A, B):
        F = [[i + j if i * j == 0 else 0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    F[i][j] = F[i - 1][j - 1]
                else:
                    F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])
        return F[len(A)][len(B)]

    for p in permutation(inputArray):
        tmp = []
        for i in range(1, len(p)):
            if levenstein(p[i - 1], p[i]) == 1:
                tmp.append(1)
                continue
            else:
                break
        if set(tmp) == {1} and len(tmp) == len(p)  - 1:
            return True
    return False
