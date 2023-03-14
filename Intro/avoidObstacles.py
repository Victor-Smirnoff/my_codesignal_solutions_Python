# https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5
# avoidObstacles
# You are given an array of integers representing coordinates of obstacles situated on a straight line.
# Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.
# Find the minimal length of the jump enough to avoid all the obstacles.
# Example
# For inputArray = [5, 3, 6, 7, 9], the output should be
# solution(inputArray) = 4.

def solution(inputArray):
    step = 1
    flag = False
    lst_out = []
    while flag == False or lst_out == []:
        lst_out = []
        flag = True
        for i in range(0, max(inputArray) + step, step):
            if i not in inputArray:
                lst_out.append(i)
            else:
                flag = False
                step += 1
                break

    return lst_out[1]
