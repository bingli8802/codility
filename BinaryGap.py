# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    br = str(bin(N))[2:]
    res = 0
    cur = 0
    for i in range(1, len(br)-1):
        if br[i] == "0":
            if br[i-1] == "1" or cur != 0:
                cur += 1
            if br[i+1] == "1":
                res = max(res, cur)
                cur = 0
    return res
