# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    i = 1
    res = float("inf")
    while i * i < N:
        if N % i == 0:
            perimeter = 2 * (i + N // i)
            res = min(res, perimeter)
        i += 1
    if i * i == N:
        res = min(res, 4 * i)
    return res
