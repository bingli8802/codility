# 自己解法不对
def solution(A):
    # write your code in Python 3.6
    sumA = [0] * (len(A) + 1)
    min_avg = (A[0] + A[1]) // 2
    pos = 0
    for i in range(1, len(A)+1):
        sumA[i] = sumA[i-1] + A[i-1]
    for i in range(len(sumA)-2):
        for j in range(i+2, len(sumA)):
            cur_sum = sumA[j] - sumA[i]
            cur_avg = cur_sum / (j-i)
            if  cur_avg < min_avg:
                min_avg = cur_avg
                pos = j-2
    return pos 

# 超时
from functools import reduce
def solution(A):
    # write your code in Python 3.6
    lenp = len(A)
    slicesum = 0
    d = {}
    l =[]
    for i in range(lenp-1):#i = 0
        for j in range(i+1,lenp): #j = 1
            slicesum = (reduce(lambda x, y: x+y, A[i:j+1]))/(j-i+1)
            l.append(slicesum)
            d[i] = min(l)
    return min(d.items(), key=lambda x: x[1])[0] #返回一個字典中值最小的鍵

# (1) There must be some slices, with length of two or three, having the minimal average value among all the slices.
# (2) And all the longer slices with minimal average are built up with these 2-element and/or 3-element small slices.
# 1、在所有的子序列中一定存在长度为2或者3的序列含有全局最小平均值
# 2、所有的长序列都可以切分为长度为2或者3的子序列
# 所以不要问：为什么不能按4个或者更多元素来进行切分，因为它们可以被切分为长度为2或者3的子序列

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    min_avg = (A[0] + A[1]) / 2.0
    min_pos = 0

    for i in range(len(A)-2):
        if (A[i] + A[i+1]) / 2.0 < min_avg:
            min_avg = (A[i] + A[i+1]) / 2.0
            min_pos = i
        if (A[i] + A[i+1] + A[i+2]) / 3.0 < min_avg:
            min_avg = (A[i] + A[i+1] + A[i+2]) / 3.0
            min_pos = i
    if (A[-1] + A[-2]) / 2.0 < min_avg:
        min_avg = (A[-1] + A[-2]) / 2.0
        min_pos = len(A) - 2
    return min_pos

