# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    d, m = divmod(Y-X, D)
    if d == 0 and m == D:
        return 0
    elif m == 0:
        return d
    else:
        return d + 1
