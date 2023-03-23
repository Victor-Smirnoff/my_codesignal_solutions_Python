# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/KeMqde6oqfF5wBXxf
# Array Packing
# You are given an array of up to four non-negative integers, each less than 256.
# Your task is to pack these integers into one number M in the following way:
# The first element of the array occupies the first 8 bits of M;
# The second element occupies next 8 bits, and so on.
# Return the obtained integer M.
# Note: the phrase "first bits of M" refers to the least significant bits of M - the right-most bits of an integer. 
# For further clarification see the following example.
# Example
# For a = [24, 85, 0], the output should be solution(a) = 21784.
# An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.
# After packing these into one number we get 00000000 01010101 00011000 (spaces are placed for convenience), which equals to 21784.

def solution(a):
    a = [bin(a[i])[2:] for i in range(len(a))][::-1]
    a = ['0' * (8 - len(a[i])) + a[i] if len(a[i]) != 8 else a[i] for i in range(len(a))]
    return int(''.join(a), 2)
