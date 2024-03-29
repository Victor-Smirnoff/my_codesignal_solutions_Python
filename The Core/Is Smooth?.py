# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/3LmZafR9wMCWpdgra
# Is Smooth?
# We define the middle of the array arr as follows:
# if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;
# if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting 
# from the beginning and from the end of the array differ by one.
# An array is called smooth if its first and its last elements are equal to one another and to the middle. 
# Given an array arr, determine if it is smooth or not.
# Example
# For arr = [7, 2, 2, 5, 10, 7], the output should be solution(arr) = true.
# The first and the last elements of arr are equal to 7, and its middle also equals 2 + 5 = 7. Thus, the array is smooth and the output is true.
# For arr = [-5, -5, 10], the output should be solution(arr) = false.
# The first and middle elements are equal to -5, but the last element equals 10. Thus, arr is not smooth and the output is false.

def solution(arr):
    return (True if arr[int(len(arr) / 2)] == arr[0] == arr[-1] else False) if len(arr) % 2 != 0 else (True if arr[int(len(arr) / 2)] + arr[int(len(arr) / 2) - 1] == arr[0] == arr[-1] else False)
