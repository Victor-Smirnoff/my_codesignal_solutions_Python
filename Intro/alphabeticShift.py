# https://app.codesignal.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui
# alphabeticShift
# Given a string, your task is to replace each of its characters by the next one in the English alphabet; 
# i.e. replace a with b, replace b with c, etc (z would be replaced by a).
# Example
# For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

def solution(inputString):
    n = 1
    return ''.join([chr(ord(x) + n - 26) if ord(x) + n > 122 else chr(ord(x) + n) for x in inputString])
