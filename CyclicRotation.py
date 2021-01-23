# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0 or K == 0:
        return A 
    k = K % len(A) 
    if k == 0:
        return A 
    else:
        return A[(len(A)-k):] + A[:(len(A)-k)]
