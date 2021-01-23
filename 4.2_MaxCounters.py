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

# O(N+M)
def solution(N, A):
    # write your code in Python 3.6
    counters = [0] * N
    max_counter = 0
    last_update = 0
    for a in A:
        if a != N + 1:
            counters[a-1] = max(counters[a-1], last_update)
            counters[a-1] += 1
            max_counter = max(counters[a-1], max_counter)
        else:
            last_update = max_counter
    for i in range(N):
        counters[i] = max(counters[i], last_update)
    return counters
