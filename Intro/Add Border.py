# https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
# Given a rectangular matrix of characters, add a border of asterisks(*) to it.
# Example
# For
# picture = ["abc",
#            "ded"]
# the output should be
# solution(picture) = ["*****",
#                      "*abc*",
#                      "*ded*",
#                      "*****"]

def solution(picture):
    picture = ["*" + picture[i] + "*" for i in range(len(picture))]
    n = len(picture[0])
    picture = ["*" * n] + picture
    picture.append("*" * n)
    return picture
