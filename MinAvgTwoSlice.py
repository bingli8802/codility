自己解法不对
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
