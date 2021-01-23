# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []
    if len(S) == 0:
        return 1
    for s in S:
        if s == "(":
            stack.append(s)
        else:
            if not stack:
                return 0
            else:
                stack.pop()
    return 1 if stack == [] else 0
