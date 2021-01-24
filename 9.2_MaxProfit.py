# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0
    dp0 = 0
    dp1 = -A[0]
    for i in range(1, len(A)):
        dp0 = max(dp0, dp1 + A[i])
        dp1 = max(dp1, -A[i])
    return dp0
