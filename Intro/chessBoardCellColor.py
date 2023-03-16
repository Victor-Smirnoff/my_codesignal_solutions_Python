# https://app.codesignal.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi
# chessBoardCellColor
# Given two cells on the standard chess board, determine whether they have the same color or not.
# Example
# For cell1 = "A1" and cell2 = "C3", the output should be
# solution(cell1, cell2) = true.
# For cell1 = "A1" and cell2 = "H3", the output should be
# solution(cell1, cell2) = false.

def solution(cell1, cell2):
    L = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    D = {'8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1}
    return True if (L[cell1[0]] + D[cell1[1]]) % 2 == (L[cell2[0]] + D[cell2[1]]) % 2 else False
