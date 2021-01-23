# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(A):
    # write your code in Python 3.6
    dic = dict(collections.Counter(A))
    for i, v in dic.items():
        if v % 2 == 1:
            return i
