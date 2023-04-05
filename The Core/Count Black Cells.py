# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/RcK4vupi8sFhakjnh
# Count Black Cells
# Imagine a white rectangular grid of n rows and m columns divided into two parts 
# by a diagonal line running from the upper left to the lower right corner. 
# Now let's paint the grid in two colors according to the following rules:
# A cell is painted black if it has at least one point in common with the diagonal;
# Otherwise, a cell is painted white.
# Count the number of cells painted black.
# Example
# For n = 3 and m = 4, the output should be solution(n, m) = 6.
# There are 6 cells that have at least one common point with the diagonal and therefore are painted black.
# For n = 3 and m = 3, the output should be solution(n, m) = 7.
# 7 cells have at least one common point with the diagonal and are painted black.

def solution(n, m):
    def my_gcd(a, b):
        return max([i for i in range(1, max(a, b) + 1) if a % i == 0 and b % i == 0])

    return n + m + my_gcd(n, m) - 2
