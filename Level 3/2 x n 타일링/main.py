def solution(n):
    prev, answer = 1, 2
    if n == 1:
        return prev
    for i in range(3, n+1):
        prev, answer = answer, (prev+answer)%1000000007
    return answer