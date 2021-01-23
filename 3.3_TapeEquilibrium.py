# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    sumA = sum(A)
    prefix = A[0]
    diff = float('inf')
    for p in range(1, len(A)):
        rem = sumA - prefix
        diff = min(abs(prefix - rem), diff)
        prefix += A[p]  
    return diff
