def solution(n):
    answer = [[1]*(n+1)]+[[0 for i in range(n+1)] for j in range(n)]
    for i in range(1, n+1):
        for j in range(i, n+1):
            answer[i][j] = answer[i][j-1]+answer[i-1][j]
    
    return answer[n][n]