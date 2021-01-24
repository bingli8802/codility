# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections
def solution(A):
    # write your code in Python 3.6
    dic = dict(collections.Counter(A))
    leader, times = max(dic.items(), key = lambda x: x[1])

    left = 0
    equiCnt = 0
    for i, v in enumerate(A):
        if v == leader:
            left += 1
        if left > (i+1) / 2 and (times-left) > (len(A)-i-1) / 2:
            equiCnt += 1
    return equiCnt
