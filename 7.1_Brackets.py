# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    left_bracket = ["(", "[", "{"]
    dic_bracket = {"(":")", "[":"]", "{":"}"}
    stack = []

    if len(S) == 0:
        return 1

    for s in S:
        if s in left_bracket:
            stack.append(s)
        else:
            try:
                if dic_bracket[stack[-1]] == s:
                    stack.pop()
                else:
                    return 0
            except IndexError:
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0
