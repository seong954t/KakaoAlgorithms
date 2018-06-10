def solution(n):
    answer = 0
    answer = list(str(n))
    answer = sorted(answer, reverse=True)
    return int(''.join(answer))