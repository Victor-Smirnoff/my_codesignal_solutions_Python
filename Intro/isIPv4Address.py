# https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso
# isIPv4Address
# An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol 
# for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.
# Given a string, find out if it satisfies the IPv4 address naming rules.
# Example
# For inputString = "172.16.254.1", the output should be
# solution(inputString) = true;
# For inputString = "172.316.254.1", the output should be
# solution(inputString) = false.
# 316 is not in range [0, 255].
# For inputString = ".254.255.0", the output should be
# solution(inputString) = false.
# There is no first number.

def solution(inputString):
    accran = list(map(str, range(256)))
    inputString = inputString.split('.')
    if len(inputString) != 4:
        return False
    if len([inputString[i] for i in range(len(inputString)) if inputString[i].isdigit()]) != 4:
        return False
    if ''.join(inputString).isdigit() == False:
        return False
    if len(inputString) != len([True for i in range(len(inputString)) if inputString[i] in accran]):
        return False
    return True
