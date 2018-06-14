def solution(n, money):
    money.sort()
    answer = [0]*(n+1)
    for coin in money:
        answer[coin]+=1
        for i in range(coin+1,n+1):
            answer[i] += answer[i-coin]
    return answer[n]