def noOvertime(n, works):
    for i in range(n):
        works[works.index(max(works))] -= 1
    
    # 야근 지수를 최소화 하였을 때의 야근 지수는 몇일까요?
    return sum([i*i for i in works])