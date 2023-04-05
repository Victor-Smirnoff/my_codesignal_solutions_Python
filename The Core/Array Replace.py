# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/mCkmbxdMsMTjBc3Bm
# Array Replace
# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
# Example
# For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
# solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

def solution(inputArray, elemToReplace, substitutionElem):
    return [inputArray[i] if inputArray[i] != elemToReplace else substitutionElem for i in range(len(inputArray))]
