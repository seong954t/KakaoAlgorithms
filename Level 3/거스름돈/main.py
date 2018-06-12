def solution(n, money):
    answer = [[0 for i in range(len(money))] for j in range(n)]
    for i in range(n):
        for j in range(len(money)):
            if money[j]-1 <= i:
                for k in range(j, len(money)):
                    if money[j]-1 == i:
                        answer[i][j] = 1
                    else:
                        answer[i][j] += answer[i-money[j]][k]
    return sum(answer[n-1])