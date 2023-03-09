# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ

# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

# For n = 1230, the output should be
# solution(n) = true;
# For n = 239017, the output should be
# solution(n) = false.

def solution(n):
    n = str(n)
    left = int(n[:int(len(n) / 2)])
    right = int(n[int(len(n) / 2):])

    count_left = 0
    while left > 0:
        count_left += left % 10
        left //= 10

    count_right = 0
    while right > 0:
        count_right += right % 10
        right //= 10

    return True if count_left == count_right else False
