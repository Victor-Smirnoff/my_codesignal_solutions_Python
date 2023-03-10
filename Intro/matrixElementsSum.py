# https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr

# After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

def solution(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for k in range(i, len(matrix)):
                    matrix[k][j] = 0
    res = 0
    for i in range(len(matrix)):
        res += sum(matrix[i])
    return res
