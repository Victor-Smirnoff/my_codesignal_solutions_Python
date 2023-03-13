# https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg
# arrayChange
# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
# Example
# For inputArray = [1, 1, 1], the output should be
# solution(inputArray) = 3.

def solution(inputArray):
    count = 0
    for i in range(len(inputArray) - 1):
        while inputArray[i] >= inputArray[i + 1]:
            x = inputArray[i] - inputArray[i + 1] + 1
            inputArray[i + 1] += x
            count += x
    
    return count
