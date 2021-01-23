def solution(S, P, Q):
    # write your code in Python 3.6
    impact_factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    result = []
    for i, j in zip(P, Q):
        result.append(impact_factor[min(list(S[i: j+1]))])
    return result
    
def solution(S, P, Q):
    # write your code in Python 3.6
    res = []
    for i in range(len(P)):
        if 'A' in S[P[i]:Q[i]+1]:
            res.append(1)
        elif 'C' in S[P[i]:Q[i]+1]:
            res.append(2)
        elif 'G' in S[P[i]:Q[i]+1]:
            res.append(3)
        else:
            res.append(4)
    return res
