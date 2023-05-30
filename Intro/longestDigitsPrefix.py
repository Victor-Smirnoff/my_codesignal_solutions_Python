# longestDigitsPrefix
# https://app.codesignal.com/arcade/intro/level-9/AACpNbZANCkhHWNs3/drafts
# Given a string, output its longest prefix which contains only digits.
# Example
# For inputString = "123aa1", the output should be solution(inputString) = "123".

def solution(inputString):
    counter = 0
    for x in inputString:
        if x.isdigit():
            counter += 1
        else:
            break
    return inputString[:counter]
