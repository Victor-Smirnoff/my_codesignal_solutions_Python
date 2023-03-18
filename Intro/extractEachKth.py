# https://app.codesignal.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R
# extractEachKth
# Given array of integers, remove each kth element from it.
# Example
# For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
# solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

def solution(inputArray, k):
    if k == 1:
        return []

    res = []
    iteration = 1
    for i in range(len(inputArray)):
        if i != k * iteration - 1:
            res.append(inputArray[i])
        else:
            iteration += 1

    return res
