# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG

# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

# Example

# For sequence = [1, 3, 2, 1], the output should be
# solution(sequence) = false.

# There is no one element in this array that can be removed in order to get a strictly increasing sequence.

# For sequence = [1, 3, 2], the output should be
# solution(sequence) = true.

# You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

def del_more(sequence):
    for i in range(1, len(sequence)):
        if sequence[i - 1] < sequence[i]:
            continue
        del sequence[i - 1]
        break
    return sequence


def del_less(sequence):
    for i in range(1, len(sequence)):
        if sequence[i - 1] < sequence[i]:
            continue
        del sequence[i]
        break
    return sequence

def solution(sequence):
    s1 = sequence[:]
    s2 = sequence[:]
    sequence1 = del_more(s1)
    sequence2 = del_less(s2)

    flag1 = True
    for i in range(1, len(sequence1)):
        if sequence1[i - 1] >= sequence1[i]:
            flag1 = False
            break
        continue

    flag2 = True
    for i in range(1, len(sequence2)):
        if sequence2[i - 1] >= sequence2[i]:
            flag2 = False
            break
        continue

    return True if flag1 or flag2 else False
