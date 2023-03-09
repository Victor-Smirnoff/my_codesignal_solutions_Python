# https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM

# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

def solution(a):
    if -1 not in a:
        return sorted(a)
    indx = [i for i in range(len(a)) if a[i] == -1]
    a = sorted(a)
    indx_tmp = [i for i in range(len(a)) if a[i] == -1]
    a = a[indx_tmp[-1] + 1:]
    for i in indx:
        a.insert(i, -1)
    return a
