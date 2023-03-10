# https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6
# Write a function that reverses characters in (possibly nested) parentheses in the input string.
# Input strings will always be well-formed with matching ()s.
# Example
# For inputString = "(bar)", the output should be
# solution(inputString) = "rab";
# For inputString = "foo(bar)baz", the output should be
# solution(inputString) = "foorabbaz";
# For inputString = "foo(bar)baz(blim)", the output should be
# solution(inputString) = "foorabbazmilb";
# For inputString = "foo(bar(baz))blim", the output should be
# solution(inputString) = "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

def solution(inputString):
    left = []

    for i in range(len(inputString)):
        if inputString[i] == '(':
            left.append(i)
        else:
            if inputString[i] == ')':
                temp = inputString[left[-1]:i + 1]
                inputString = inputString[:left[-1]] + temp[::-1] + inputString[i + 1:]
                del left[-1]

    res = ''
    for i in range(len(inputString)):
        if inputString[i] != '(' and inputString[i] != ')':
            res += inputString[i]

    return res  
