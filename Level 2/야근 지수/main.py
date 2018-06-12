def solution(n, works):
    if sum(works) < n:
        return 0
    for i in range(n):
        works[works.index(max(works))] -= 1
    return sum([i*i for i in works])