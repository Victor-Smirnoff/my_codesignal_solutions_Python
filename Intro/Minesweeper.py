# https://app.codesignal.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM
# Minesweeper
# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates 
# the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.
# Example
# For
# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]
# the output should be
# solution(matrix) = [[1, 2, 1],
#                     [2, 1, 1],
#                     [1, 1, 1]]

def solution(matrix):
    res = [[0] * len(matrix[k]) for k in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == True:
                if j - 1 in range(j):
                    res[i][j - 1] += 1
                if j + 1 in range(len(matrix[i])):
                    res[i][j + 1] += 1
                if i - 1 in range(i):
                    res[i - 1][j] += 1
                if i + 1 in range(len(matrix)):
                    res[i + 1][j] += 1
                if i - 1 in range(i) and j - 1 in range(j):
                    res[i - 1][j - 1] += 1
                if i - 1 in range(i) and j + 1 in range(len(matrix[i])):
                    res[i - 1][j + 1] += 1
                if i + 1 in range(len(matrix)) and j - 1 in range(j):
                    res[i + 1][j - 1] += 1
                if i + 1 in range(len(matrix)) and j + 1 in range(len(matrix[i])):
                    res[i + 1][j + 1] += 1

    return res
