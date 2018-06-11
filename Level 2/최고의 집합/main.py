def solution(n, s):
    answer = []
    share = s//n
    remainder = s%n
    if share == 0:
        return [-1]
    answer = [share]*(n-remainder)
    if s%n == 0:
        return answer
    return answer + solution(remainder, s-share*(n-remainder))