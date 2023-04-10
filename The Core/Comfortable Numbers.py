# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/pNfGgNk46YZ4c4RW5
# Comfortable Numbers
# Let's say that number a feels comfortable with number b if a ≠ b and b lies in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.
# How many pairs (a, b) are there, such that a < b, both a and b lie on the segment [l, r], 
# and each number feels comfortable with the other (so a feels comfortable with b and b feels comfortable with a)?
# Example
# For l = 10 and r = 12, the output should be solution(l, r) = 2.
# Here are all values of s(x) to consider:
# s(10) = 1, so 10 is comfortable with 9 and 11;
# s(11) = 2, so 11 is comfortable with 9, 10, 12 and 13;
# s(12) = 3, so 12 is comfortable with 9, 10, 11, 13, 14 and 15.
# Thus, there are 2 pairs of numbers comfortable with each other within the segment [10; 12]: (10, 11) and (11, 12).

def solution(l, r):
    def get_sum(n):
        sum_n = 0
        while n > 0:
            sum_n += (n % 10)
            n //= 10
        return sum_n

    res = []
    for a in range(l, r):
        b = list(range(a - get_sum(a), a + get_sum(a) + 1))
        for i in b:
            if a < i and a != i and l <= a and i <= r and a in list(range(i - get_sum(i), i + get_sum(i) + 1)):
                res.append((a, i))

    return len(res)
