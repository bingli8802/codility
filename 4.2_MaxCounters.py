# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(N*M)
def solution(N, A):
    # write your code in Python 3.6
    arr = [0] * N
    for a in A:
        if a != N + 1:
            arr[a-1] += 1
        else:
            arr = [max(arr)] * N
    return arr
