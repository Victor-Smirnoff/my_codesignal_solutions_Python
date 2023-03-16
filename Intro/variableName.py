# https://app.codesignal.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno
# variableName
# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.
# Check if the given string is a correct variable name.
# Example
# For name = "var_1__Int", the output should be
# solution(name) = true;
# For name = "qq-q", the output should be
# solution(name) = false;
# For name = "2w2", the output should be
# solution(name) = false.

from string import ascii_letters, digits
allowed_chars_first = ascii_letters + '_'
allowed_chars_all = ascii_letters + '_' + digits

def solution(name):
    if name[0] not in allowed_chars_first:
        return False
    return False if [name[i] for i in range(len(name)) if name[i] not in allowed_chars_all] else True
