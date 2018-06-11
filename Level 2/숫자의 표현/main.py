def solution(n):
    answer = 0
    for i in range(1, n//2+1):
        if i % 2 == 0:
            if n%i == i//2 and n//i > i//2:
                answer += 1
        else:
            if n%i == 0 and n//i > i//2:
                answer += 1
    return answer