# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    sumN = (N + 1) * (N + 2) // 2 - sum(A)
    return sumN 
