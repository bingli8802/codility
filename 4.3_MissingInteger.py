# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A_set = set(A)
    for i in range(1, len(A_set)+1):
        if i not in A_set:
            return i
    return len(A_set) + 1
