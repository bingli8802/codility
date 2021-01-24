# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    dp = [0] * n
    dp[0] = A[0]
    for i in range(1, n):
        dp[i] = max(A[i], A[i]+dp[i-1])
    return max(dp)
  
# MaxNonnegSliceSum
