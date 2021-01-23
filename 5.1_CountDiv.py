def solution(A, B, K):
    # write your code in Python 3.6
    return B // K - A // K + (not A % K)
