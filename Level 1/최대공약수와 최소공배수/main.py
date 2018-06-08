def solution(n, m):
    answer = n*m
    if n < m:
        (n, m) = (m, n)
    while m != 0:
        (n, m) = (m, n%m)
    answer = [n, int(answer//n)]
    return answer