# MinDistinct

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    i = 1
    res = 0
    while i * i < N:
        if N % i == 0:
            res += 2
        i += 1
    if i * i == N:
        res += 1
    return res
