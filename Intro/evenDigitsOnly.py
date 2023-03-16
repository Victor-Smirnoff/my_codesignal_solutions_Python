# https://app.codesignal.com/arcade/intro/level-6/6cmcmszJQr6GQzRwW
# evenDigitsOnly
# Check if all digits of the given integer are even.
# Example
# For n = 248622, the output should be
# solution(n) = true;
# For n = 642386, the output should be
# solution(n) = false.

def solution(n):
    return False if [x for x in list(map(int, list(str(n)))) if x % 2 != 0] else True
