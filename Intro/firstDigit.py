# https://app.codesignal.com/arcade/intro/level-8/rRGGbTtwZe2mA8Wov
# firstDigit
# Find the leftmost digit that occurs in a given string.
# Example
# For inputString = "var_1__Int", the output should be
# solution(inputString) = '1';
# For inputString = "q2q-q", the output should be
# solution(inputString) = '2';
# For inputString = "0ss", the output should be
# solution(inputString) = '0'.

def solution(inputString):
    return [num for num in inputString if num.isdigit()][0]
