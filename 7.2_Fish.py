Put all downstream swimming fishes on a stack. Any upstream swimming fish has to fight(eat) all fishes on the stack. 
If there is no fish on the stack, the fish survives. If the stack has some downstream fishes at the end, they also survive.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    alive = 0
    stack = []
    for i, v in enumerate(B):
        if v == 0:
            while len(stack) != 0:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                alive += 1
        else:
            stack.append(A[i])
    return alive + len(stack)
