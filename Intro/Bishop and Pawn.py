# Bishop and Pawn
# https://app.codesignal.com/arcade/intro/level-9/6M57rMTFB9MeDeSWo/solutions
# Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.
# The bishop has no restrictions in distance for each move, but is limited to diagonal movement.
# Example
# For bishop = "a1" and pawn = "c3", the output should be solution(bishop, pawn) = true.
# For bishop = "h1" and pawn = "h3", the output should be solution(bishop, pawn) = false.


def solution(bishop, pawn):
    d_letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6,  "h": 7}
    d_digits = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6,  "1": 7}

    coord_bishop = (d_letters[bishop[0]], d_digits[bishop[1]])
    coord_pawn = (d_letters[pawn[0]], d_digits[pawn[1]])

    matrix = [[0] * 8 for _ in range(8)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (j, i) == coord_bishop:
                matrix[i][j] = "B"

    x, y = coord_bishop
    while True:
        x += 1
        y += 1
        if x <= 7 and y <= 7:
            matrix[y][x] = "*"
        else:
            break

    x, y = coord_bishop
    while True:
        x -= 1
        y -= 1
        if x >= 0 and y >= 0:
            matrix[y][x] = "*"
        else:
            break

    x, y = coord_bishop
    while True:
        x += 1
        y -= 1
        if x <= 7 and y >= 0:
            matrix[y][x] = "*"
        else:
            break

    x, y = coord_bishop
    while True:
        x -= 1
        y += 1
        if x >= 0 and y <= 7:
            matrix[y][x] = "*"
        else:
            break

    return matrix[coord_pawn[1]][coord_pawn[0]] == "*"
