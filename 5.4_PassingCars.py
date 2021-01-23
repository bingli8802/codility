# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pairs = 0
    west_cars = 0
    for i in range(len(A)-1, -1, -1):
        if A[i] == 1:
            west_cars += 1
        else:
            pairs += west_cars
            if pairs > 1000000000:
                return -1
    return pairs
