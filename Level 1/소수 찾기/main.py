def solution(n):
    result = [False, False]+[True]*(n-1)
    for i in range(2, (n+1)//2):
        for j in range(i+i, n+1, i):
            result[j] = False
    return result.count(True)